# MLoggers

This package offers a collection of loggers well suited for machine learning experiments.

## Getting started

You can download the package via `pip install mloggers`. Dependencies include:

- `numpy`
- `termcolor`
- `wandb` (for integration with Weights & Biases)
- `omegaconf` (for integration with Hydra via Weights & Biases)

## Usage

Example usage (with Hydra integration):

```python
import time

from mloggers import LoggerType, MultiLogger
from omegaconf import DictConfig


@hydra.main(version_base=None, config_path="configs", config_name="train")
def main(config: DictConfig):
    # Create a multi-logger
    logger = MultiLogger(
        loggers=[LoggerType.CONSOLE, LoggerType.WANDB],
        run_id=str(int(time.time())),
        project_name="Research-Project",
        group_name="Interesting-Experiments",
        experiment_name="Experiment-1",
        config=config,
    )

    # Run an experiment
    logger.info("Starting the experiment")
    try:
        results = run_experiment(config, logger)
    except Exception as e:
        logger.error({"Exception occurred during training": e})
        results = {}
    logger.info(
        {
            "Experiment finished": None,
            "Experiment results": results,
        }
    )

    # Close the logger
    logger.close()
```

### Built-in loggers

At this moment, the supported loggers are:

- `Filelogger`: records logs to a file.
- `ConsoleLogger`: records logs to the console.
- `WandbLogger`: sends logs to a Weights & Biases project; requires an API key.
- `MultiLogger`: aggregates any/all of the above loggers to record the same messages through multiple channels in a single `log()` call.

The available methods to log messages are:

- `log(message, level, mask)`: logs a message of a given level (`INFO`, `WARNING` or `ERROR`), where the mask is used by the `MultiLogger` to filter loggers which are not supposed to record the message.
- `info(message, mask)`: wrapper to call `log(message, "INFO", mask)`.
- `warn(message, mask)`: wrapper to call `log(message, "WARNING", mask)`.
- `error(message, mask)`: wrapper to call `log(message, "ERROR", mask)`.
- `close()`: perform all necessary actions before destroying a logger.

### Customized loggers

You can extend the base class `Logger` in order to create a custom logger to suit your own needs. Make sure to implement all abstract methods.
