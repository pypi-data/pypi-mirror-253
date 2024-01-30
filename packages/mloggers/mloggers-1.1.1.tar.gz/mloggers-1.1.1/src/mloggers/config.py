from dataclasses import dataclass
from enum import Enum

from hydra.core.config_store import ConfigStore


# NOTE: When https://github.com/omry/omegaconf/issues/422 is done, we could
#       use typing.Literal instead of this aberration
class StrEnum(str, Enum):
    def __str__(self) -> str:
        return self.value


class LoggerName(StrEnum):
    console = "console"
    file = "file"
    wandb = "wandb"


@dataclass(kw_only=True)
class LoggerConfig:
    """
    Configuration for the logger.
    """

    project_name: str = "Project"
    """Name of the project."""

    group_name: str = "Group"
    """Name of the group."""

    experiment_name: str = "Name"
    """Name of the group."""

    run_id: str = "generic-ID"
    """ID of the experiment, should be uniquely set at runtime."""

    loggers: str = "console"
    """List of loggers to use, of type `LoggerName`. Multiple loggers are separated by commas, e.g.: "console,wandb"."""

    default_mask: LoggerName = LoggerName.wandb
    """Default mask to be used by the multi-logger."""

    interval: int = 1
    """How often to log the progress."""


cs = ConfigStore.instance()
cs.store(name="base_logger", node=LoggerConfig)
