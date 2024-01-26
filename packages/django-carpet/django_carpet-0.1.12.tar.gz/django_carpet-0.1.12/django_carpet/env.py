# Django
from django.conf import settings

# Foundation
from .choices import EnvChoices


def exec_mode() -> str:
    """Gets the `EXEC_MODE` variable from the settings, informing the current state of runtime

    Returns:
        A member of `EnvChoices`
    """
    return getattr(settings, "EXEC_MODE", EnvChoices.NORMAL)


def is_debug() -> bool:
    return settings.DEBUG