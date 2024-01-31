from typing import Any, Dict, Optional, Union

import wandb
from omegaconf import DictConfig
from termcolor import colored

from .logger import Logger


class WandbLogger(Logger):
    """Logs to Weights & Biases."""

    def __init__(
        self, project: str, group: str, name: str, id: str, config: Optional[DictConfig]
    ):
        """
        Initializes a Weights & Biases logger.

        ### Parameters
        ----------
        `project` -> the name of the project to log to.
        `group` -> the name of the group to log to.
        `experiment` -> the ID of the experiment to log to.
        [optional] `config` -> the configuration of the experiment.
        """

        super().__init__()
        if config is not None:
            config = vars(config)
        wandb.init(project=project, group=group, name=name + "_" + id, config=config)

    def _log_impl(self, message: Union[str, Dict[str, Any]], level: str = "INFO", *_):
        """
        Logs a message to Weights & Biases.

        ### Parameters
        ----------
        `message` -> the message to log.
        `level` -> the level of the message (e.g., INFO, WARNING, ERROR, DEBUG, etc.); not used for messages of type dictionary.
        [UNUSED] `mask`
        """

        try:
            if isinstance(message, str):
                log = {level: message}
            else:
                log = message
            wandb.log(log)
        except Exception as e:
            print(f'{colored("[ERROR]", "red")} Error while logging to wandb: {e}')

    def __del__(self):
        """Finishes the connection with W&B."""

        wandb.finish()
