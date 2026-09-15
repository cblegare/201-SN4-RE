from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Any


def logging_configuration(
    verbosity: int, logfile: Path | None = None
) -> dict[str, Any]:
    """
    Build logging configuration based on a verbosity level.

    Args:
        verbosity:
            Verbosity 0 is means "CRITICAL", and each increments move
            toward "DEBUG".
        logfile:
            Optional log file.

    """
    level = max(logging.CRITICAL - logging.DEBUG * verbosity, logging.DEBUG)

    formatters = {
        "standard": {"format": "%(levelname)8s: %(message)s"},
        "debug": {"format": "%(levelname)8s %(name)-16s:%(funcName)-12s> %(message)s"},
    }

    active_formatter = "debug" if level <= logging.DEBUG else "standard"

    handlers = {
        "console": {
            "level": level,
            "formatter": active_formatter,
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",  # Default is stderr
        },
    }

    if logfile:
        handlers["file"] = {
            "level": level,
            "formatter": active_formatter,
            "class": "logging.FileHandler",
            "filename": str(logfile),
        }

    loggers = {
        "": {
            # root logger
            "handlers": handlers.keys(),
            "level": level,
            "propagate": True,
        }
    }

    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": formatters,
        "handlers": handlers,
        "loggers": loggers,
    }
