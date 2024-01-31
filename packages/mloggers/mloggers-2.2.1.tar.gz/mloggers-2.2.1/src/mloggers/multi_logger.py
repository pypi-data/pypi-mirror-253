from typing import Any, Dict, Optional, Union

from omegaconf import DictConfig
from termcolor import colored

from . import LoggerType
from .console_logger import ConsoleLogger
from .file_logger import FileLogger
from .logger import Logger
from .wandb_logger import WandbLogger


class MultiLogger(Logger):
    """Logs to multiple loggers."""

    def __init__(
        self,
        loggers: list[LoggerType],
        run_id: str = "id",
        project_name: str = "project",
        group_name: str = "group",
        experiment_name: str = "experiment",
        default_mask: list[LoggerType] = [],
        config: Optional[DictConfig] = None,
    ):
        """
        Initializes a multi-logger.

        ### Parameters
        ----------
        `loggers` -> a list of the loggers to use.
        `run_id` -> the ID of the run.
        `project_name` -> the name of the project to log to.
        `group_name` -> the name of the group to log to.
        `experiment_name` -> the name of the experiment to log to.
        `default_mask` -> the default mask to use when logging.
        [optional] `config` -> the configuration of the experiment (for W&B).
        """

        super().__init__(default_mask)

        loggers = {}
        for logger in loggers:
            if logger == LoggerType.CONSOLE:
                loggers["console"] = ConsoleLogger()
            elif logger == LoggerType.FILE:
                loggers["file"] = FileLogger(
                    project_name,
                    group_name,
                    experiment_name,
                    run_id,
                )
            elif logger == LoggerType.WANDB:
                loggers["wandb"] = WandbLogger(
                    project_name,
                    group_name,
                    experiment_name,
                    run_id,
                    config,
                )
            elif logger == "":
                pass
            else:
                print(
                    f'{colored("[WARNING]", "yellow")} Logger "{logger}" is not supported'
                )

        self._loggers = loggers

    def _log_impl(
        self,
        message: Union[str, Dict[str, Any]],
        level: str = "INFO",
        mask: list[LoggerType] = [],
    ):
        """
        Logs a message to multiple loggers.

        ### Parameters
        ----------
        `message` -> the message to log.
        `level` -> the level of the message (e.g., INFO, WARNING, ERROR, DEBUG, etc.).
        `mask` -> a list of logger names to not be used to log this message.
        """

        for logger in [
            logger
            for logger_name, logger in self._loggers.items()
            if logger_name not in mask
        ]:
            logger(message, level, mask)
