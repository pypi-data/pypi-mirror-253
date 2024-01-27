"""Top-level package for Environment backups."""

__author__ = """Luis C. Berrocal"""
__email__ = 'luis.berrocal.1942@gmail.com'
__version__ = '1.5.3'

from rich.console import Console

from .config.configuration import ConfigurationManager

CONFIGURATION_MANAGER = ConfigurationManager(version=__version__)

CONSOLE = Console()


def logger_configuration():
    import logging.config

    from .constants import LOGGING

    logging.config.dictConfig(LOGGING)


logger_configuration()

# TODO Add tox support
