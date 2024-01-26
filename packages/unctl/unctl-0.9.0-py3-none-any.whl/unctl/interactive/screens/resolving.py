from typing import cast

from textual import work, on
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import (
    Static,
    Footer,
    Header,
    RichLog,
    Input,
)
from textual.containers import Container

from unctl.lib.checks.check_report import CheckReport
from unctl.interactive.screens.exec_confirm import ExecutionConfirm
from unctl.interactive.screens.preview import PreviewReturn, PreviewScreen
from unctl.scanrkube import ResourceChecker


class ResolvingScreen(Screen):
    PASSED_TITLE = "Problem is solved"
    FAILED_TITLE = "Failed item"

    BINDINGS = [
        ("d", "execute_diagnosis", "Execute diagnostics"),
        ("f", "execute_fix", "Execute fixes"),
        ("r", "re_run_check", "Re-run check for object"),
        ("escape", "app.pop_screen", "Back to table"),
    ]

    TITLE = "Resolving the problem"

    @property
    def in_progress(self) -> bool:
        return self.query_one(Input).loading

    @property
    def chat_body(self) -> RichLog:
        return cast(RichLog, self.query_one("#chatbody"))

    def __init__(self, item: CheckReport, checker: ResourceChecker):
        super().__init__()
        self._item = item
        self._checker = checker

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

        classes = ""
        title = self.FAILED_TITLE
        if self._item.passed:
            title = self.PASSED_TITLE
            classes = "passed"

        yield Container(
            Static(title, id="sidebar-title"),
            Static(self._item.display_object, id="sidebar-body"),
            id="sidebar",
            classes=classes,
        )

        yield Container(
            RichLog(wrap=True, highlight=True, markup=True, id="chatbody"),
            Input(placeholder="Send a message...", id="chatinput"),
        )

    def on_mount(self):
        self.init()

    @work()
    async def init(self):
        if not self._item.passed:
            self.print_next_steps()
        else:
            self.chat_body.write(f"{self._item.object_name} has been already fixed.")
            self.print_divider()
            self.query_one(Input).visible = False

    def print_divider(self):
        line = "-" * self.chat_body.max_width
        self.chat_body.write(f"\n{line}\n", expand=True)

    def print_next_steps(self):
        text_log = self.chat_body
        text_log.write("[bold cyan]Summary:[/bold cyan]\n")
        text_log.write(self._item.llm_summary)
        self.print_divider()

        if len(self._item.diagnosis_options) > 0:
            text_log.write("[bold cyan]Possible diagnostics:[/bold cyan]\n")
            diagnostics = "\n- ".join(self._item.diagnosis_options)
            text_log.write(f"- {diagnostics}")
            self.print_divider()

        if len(self._item.fix_options) > 0:
            text_log.write("[bold cyan]Possible fixes:[/bold cyan]\n")
            fixes = "\n- ".join(self._item.fix_options)
            text_log.write(f"- {fixes}")
            self.print_divider()

    def lock_operations(self):
        placeholder = self.query_one(Input)
        placeholder.loading = True

    def unlock_operations(self):
        placeholder = self.query_one(Input)
        placeholder.loading = False

    def action_re_run_check(self):
        if self.in_progress or self._item.passed:
            return

        self.lock_operations()
        self.chat_body.write(f"Re-running check for {self._item.object_name}...")
        self.print_divider()
        self.re_run_check()

    @work()
    async def re_run_check(self):
        # TODO: implement single object re-run
        await self._checker.execute()
        if not any(
            report
            for report in self._checker.failing_reports
            if report.object_id == self._item.object_id
        ):
            self._item.status = "PASS"

        if self._item.passed:
            title = cast(Static, self.query_one("#sidebar-title"))
            title.update(self.PASSED_TITLE)
            body = cast(Static, self.query_one("#sidebar-body"))
            body.update(self._item.display_object)
            sidebar = cast(Container, self.query_one("#sidebar"))
            sidebar.add_class("passed")
            self.print_divider()
            self.chat_body.write(f"{self._item.object_name} has been fixed. Thank you!")
            self.query_one(Input).visible = False
        else:
            self.chat_body.write(f"{self._item.object_name} still has an issue.")

        self.print_divider()
        self.unlock_operations()

        self.app.update()

    async def action_analyse_problem(self):
        if self.in_progress or self._item.passed:
            return

        self.chat_body.write(f"Analysis started for {self._item.object_name}...")
        self.print_divider()
        self.lock_operations()

        # run analyse problem method
        self.analyse_problem()

    @work()
    async def analyse_problem(self):
        await self._item.get_next_steps()
        self.unlock_operations()
        self.print_next_steps()

    async def execution_confirmed(self, commands: list[str]):
        self.lock_operations()
        self.execute_commands(commands=commands)

    async def action_execute_diagnosis(self):
        if self.in_progress or self._item.passed:
            return

        await self.app.push_screen(
            ExecutionConfirm(commands=self._item.diagnosis_options),
            self.execution_confirmed,
        )

    @work()
    async def execute_commands(self, commands: list[str]):
        self.chat_body.write("Executing commands...")
        self.print_divider()

        outputs = await self._item.execute_commands(cmds=commands)
        await self.app.push_screen(
            PreviewScreen(outputs), self.add_outputs_to_chat_body
        )

    async def add_outputs_to_chat_body(self, preview: PreviewReturn):
        for index, (key, item) in enumerate(preview.outputs.items()):
            self.chat_body.write(
                f"[bold yellow]{index+1}. {key.strip()}[/bold yellow]\n"
            )

            self.chat_body.write(item)
            self.print_divider()

        if preview.send_data:
            errors = await self._item.send_to_llm(preview.outputs)
            if len(errors) > 0:
                for cmd, error in errors.items():
                    self.chat_body.write(
                        f"Failed to send output for '{cmd}':\n"
                        f"[bold red]Reason: {error}[/bold red]"
                    )
                    self.print_divider()
            else:
                self.chat_body.write("Outputs have been sent successfuly to LLM.")
                self.print_divider()

            self.unlock_operations()
            await self.action_analyse_problem()
        else:
            self.unlock_operations()

    async def action_execute_fix(self):
        if self.in_progress or self._item.passed:
            return

        await self.app.push_screen(
            ExecutionConfirm(commands=self._item.fix_options),
            self.execution_confirmed,
        )

    @on(Input.Submitted)
    async def submit_message(self, event: Input.Submitted):
        self.chat_body.write(f"[bold green]You: [/bold green]{event.value}")
        self.print_divider()
        event.input.clear()
        self.lock_operations()

        # send message to AI
        self.ai_chat(message=event.value)

    @work()
    async def ai_chat(self, message: str):
        await self._item.get_next_steps(message=message)
        self.unlock_operations()
        self.print_next_steps()
