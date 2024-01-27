"""Console script for environment_backups."""
import logging
import sys
from platform import python_version
from typing import List

import click
from rich.panel import Panel

from environment_backups import CONFIGURATION_MANAGER, CONSOLE
from environment_backups import __version__ as current_version
from environment_backups.backups.cli_commands import backup
from environment_backups.config.cli_commands import config

logger = logging.getLogger(__name__)


@click.group()
def main():
    """Main entrypoint."""


@click.command()
def about():
    # Add available configurations
    app_name = CONFIGURATION_MANAGER.APP_NAME.replace('-', ' ').title()
    content: List[str] = [
        f'Operating System: {sys.platform}',
        f'Python : {python_version()}',
        f'Configuration file: {CONFIGURATION_MANAGER.config_file}',
    ]
    panel = Panel('\n'.join(content), title=app_name, subtitle=f"version: {current_version}")
    CONSOLE.print(panel)


# TODO add configurations and status


main.add_command(backup)
main.add_command(about)
main.add_command(config)
