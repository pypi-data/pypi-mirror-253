# MLoggers
This package offers a collection of loggers well suited for machine learning experiments.

## Built-in loggers
At this moment, the supported loggers are:
- File logger (`file_logger`): records logs to a file.
- Console logger (`console_logger`): records logs to the console.
- Weights & Biases logger (`wandb_logger`): sends logs to a W&B project; requires an API key.
- Multi-logger (`multi_logger`): aggregates any/all of the above loggers to record the same messages through multiple channels.

## Customized loggers
You can extend the base class `Logger` in order to create a custom logger to suit your own needs.
