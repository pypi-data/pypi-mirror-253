from .console_logger import ConsoleLogger
from .file_logger import FileLogger
from .logger import Logger
from .multi_logger import MultiLogger
from .wandb_logger import WandbLogger

__all__ = [
    "LoggerType",
    "ConsoleLogger",
    "FileLogger",
    "Logger",
    "MultiLogger",
    "WandbLogger",
]


class LoggerType:
    CONSOLE = "console"
    FILE = "file"
    WANDB = "wandb"
