from environment_backups import CONFIGURATION_MANAGER

DEFAULT_ENV_FOLDER = '.envs'
# FIXME This does not work. Not sure where this is being used
DEFAULT_DATE_FORMAT = '%Y%m%d_%H'

LOG_FILE = CONFIGURATION_MANAGER.logs_folder / f'{CONFIGURATION_MANAGER.APP_NAME}.log'
# TODO add line number to formatter
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {"verbose": {"format": "%(levelname)s %(asctime)s %(module)s " "%(process)d %(thread)d %(message)s"}},
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "verbose",
            "filename": str(LOG_FILE),
            "maxBytes": 1024,
            "backupCount": 3,
        },
    },
    "loggers": {
         # "root": {
         #     "level": "DEBUG",
         #     "handlers": [
         #         "console",
         #     ],
         # },
        'environment_backups': {"level": "DEBUG", "handlers": ['console', 'file'], "propagate": False},
    },
}
