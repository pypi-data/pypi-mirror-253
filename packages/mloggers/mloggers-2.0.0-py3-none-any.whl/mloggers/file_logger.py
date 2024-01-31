import json
import os
import uuid
from datetime import datetime
from typing import Any, Dict, Union

import numpy as np
from termcolor import colored

from .logger import Logger


class FileLogger(Logger):
    """Logs to a file."""

    TRIES = 10

    def __init__(self, project: str, group: str, name: str, id: str):
        """
        Initializes a file logger.

        ### Parameters
        ----------
        `project` -> the name of the project.
        `group` -> the name of the group.
        `name` -> the name of the experiment.
        `id` -> the ID of the run.
        """

        super().__init__()

        # Define file path and name
        dir_path = f"logs/{project}/{group}/"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        file_path = dir_path + name + "_" + id + ".json"

        # Use a random uuid if the file name is already taken
        while os.path.exists(file_path) and self.TRIES > 0:
            file_path = dir_path + str(uuid.uuid4()) + ".json"
            self.TRIES -= 1
        if self.TRIES == 0:
            print(
                f'{colored("[WARNING]", "yellow")} Could not create log file: too many tries. Subsequent logs will fail to be saved'
            )

        # Create the file
        with open(file_path, "x"):
            pass

        print(f'{colored("[INFO]", "cyan")} Logging to file {file_path}')

        self._file_path = file_path

    def _log_impl(self, message: Union[str, Dict[str, Any]], level: str = "INFO", *_):
        """
        Logs a message to a file.

        ### Parameters
        ----------
        `message` -> the message to log.
        `level` -> the level of the message (e.g., INFO, WARNING, ERROR, etc.).
        [UNUSED] `mask`

        ### Raises
        ----------
        `TypeError` -> if the message is not a string, a dictionary or does not implement `__str__()`.
        """

        # Convert numpy's ndarrays to lists so that they are JSON serializable
        if isinstance(message, dict):
            for key, value in message.items():
                if isinstance(value, np.ndarray):
                    message[key] = value.tolist()
        elif hasattr(message, "__str__") and callable(getattr(message, "__str__")):
            message = str(message)
        else:
            raise TypeError(
                f"Expected message to be a string, a dictionary or to have implemented __str__(), but got {type(message)}."
            )

        try:
            with open(self._file_path) as file:
                try:
                    logs = json.load(file)
                except json.decoder.JSONDecodeError:
                    logs = []

            log = {
                "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "level": level,
                "message": message,
            }
            logs.append(log)

            with open(self._file_path, "w") as file:
                file.seek(0)
                json.dump(logs, file, indent=4)

        except Exception as e:
            print(
                f'{colored("[ERROR]", "red")} Exception thrown while logging to a file: {e}'
            )

    def close(self):
        """Closes the logger."""

        return
