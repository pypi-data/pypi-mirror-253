from colorama import Fore, Style

from unctl.lib.models.checks import CheckMetadataModel


def get_severity(check: CheckMetadataModel):
    severity_color = (
        Fore.RED
        if check.Severity == "Critical"
        else (Fore.YELLOW if check.Severity == "Severe" else Fore.WHITE)
    )
    return severity_color + check.Severity + Style.RESET_ALL
