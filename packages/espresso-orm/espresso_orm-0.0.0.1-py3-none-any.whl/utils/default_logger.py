import logging
import os
import sys


# ANSI escape codes for colors
class ColoredFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": "\033[92m",  # GREEN
        "INFO": "\033[96m",  # BLUE
        "WARNING": "\033[93m",  # DARK YELLOW
        "ERROR": "\033[91m",  # RED
        "CRITICAL": "\033[91m",  # RED
        "RESET": "\033[0m",  # RESET COLOR
    }

    def format(self, record):
        log_fmt = (
            f"%(asctime)s - %(name)s - {self.COLORS[record.levelname]}"
            f"%(levelname)s{self.COLORS['RESET']}: %(message)s"
        )

        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_logger(name):
    # Configure logging
    logger = logging.getLogger(name)

    log_level = logging.DEBUG if os.environ.get("log_level") else logging.INFO

    # Handler for lower levels (INFO and below) to stdout
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.addFilter(lambda record: record.levelno <= logging.INFO)
    stdout_handler.setFormatter(ColoredFormatter())

    # Handler for higher levels (WARNING and above) to stderr
    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.WARNING)
    stderr_handler.setFormatter(ColoredFormatter())

    logger.setLevel(log_level)
    logger.addHandler(stdout_handler)
    logger.addHandler(stderr_handler)
    return logger
