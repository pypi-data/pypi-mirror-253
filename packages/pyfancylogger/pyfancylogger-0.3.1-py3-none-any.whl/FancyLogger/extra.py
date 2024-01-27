from .logger import FancyFormatter
from .colors import BRIGHT_CYAN


class Formats:
    general = '[%(levelname)s] %(name)s - %(message)s'
    timed = '%(asctime)s - [%(levelname)s] %(name)s - %(message)s'
    detailed = '%(asctime)s.%(msecs)03d - [%(levelname)s] %(name)s [%(filename)s:%(lineno)d] - %(message)s'


class Formatters:
    detailed_white = FancyFormatter(Formats.detailed)
    detailed_cyan = FancyFormatter(Formats.detailed)
    detailed_cyan.INFO = BRIGHT_CYAN

    general_white = FancyFormatter(Formats.general)
    general_cyan = FancyFormatter(Formats.general)
    general_white.INFO = BRIGHT_CYAN

    timed_white = FancyFormatter(Formats.timed)
    timed_cyan = FancyFormatter(Formats.timed)
    timed_white.INFO = BRIGHT_CYAN
