from .colors import *
from .extra import *
from .logger import *


def overwrite(formatter: Formatter = None) -> None:
    import logging

    logging.root.manager.setLoggerClass(FancyLogger)
    FancyLogger.defaultFormatter = formatter

    log_dict = logging.root.manager.loggerDict
    log_changes = {}
    for name, log in log_dict.items():
        if isinstance(log, logging.Logger) and not isinstance(log, FancyLogger):
            log_changes[name] = FancyLogger(name, formatter)
            log_changes[name].setLevel(log.level)

    for name, log in log_changes.items():
        log_dict[name] = log
