import asyncio
import sys
import time
from functools import wraps
from pathlib import Path

import click
from gdrive_pydantic_wrapper.google_drive.gdrive import GDrive
from rich.live import Live
from rich.spinner import Spinner
from rich.text import Text

from environment_backups import CONFIGURATION_MANAGER
from environment_backups.backups.backups import backup_environment, backup_envs
from environment_backups.config.configuration import get_configuration_by_name
from environment_backups.exceptions import EnvironmentBackupsError


def async_cmd(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return asyncio.run(func(*args, **kwargs))

    return wrapper


@click.command()
@async_cmd
@click.option('environment', '-e', '--environment', type=str, required=False)
@click.option('projects_folder', '-p', '--projects-folder', type=click.Path(exists=True), required=False)
@click.option('backup_folder', '-b', '--backup-folder', type=click.Path(exists=False), required=False)
@click.option('use_async', '--async', is_flag=True, default=False)
async def backup(environment: str, projects_folder: Path, backup_folder: Path, use_async: bool):
    if environment:
        start = time.time()
        app_cfg = CONFIGURATION_MANAGER.get_current()
        env_cfg, _ = get_configuration_by_name(config_name=environment, app_configuration=app_cfg)
        if env_cfg is None:
            click.secho(f'No environment configuration found for {environment}.', fg='red')
            sys.exit(100)
        zip_list, b_folder = await backup_environment(environment_name=environment, use_async=use_async)

        for i, zip_file in enumerate(zip_list, 1):
            # TODO print only on verbose mode.
            click.secho(f'{i:3}. {zip_file.name}', fg='green')

        elapsed = time.time() - start
        click.secho(f'Saved {len(zip_list)} zip environments to {b_folder}. Took {elapsed:.2f} seconds.', fg='green')

        if env_cfg.get('google_drive_folder_id'):
            # TODO add elapsed to upload
            spinner = Spinner('dots3', text=Text('Uploading to Google Drive'))
            with Live(spinner):
                secrets_file = Path(env_cfg.get('google_authentication_file'))
                gdrive = GDrive(secrets_file=secrets_file)
                gdrive.upload_folder(b_folder, env_cfg['google_drive_folder_id'])
            click.secho(f'Uploaded {b_folder} to google drive', fg='green')
    else:
        legacy_backup(backup_folder, projects_folder)


def legacy_backup(backup_folder, projects_folder):
    if projects_folder is None:
        raise EnvironmentBackupsError('Missing projects folder')
    else:
        projects_folder = Path(projects_folder)
    if backup_folder is None:
        raise EnvironmentBackupsError('Missing backup folder')
    else:
        backup_folder = Path(backup_folder)
    environment_folders = ['.envs']
    zip_list, b_folder = backup_envs(
        projects_folder=projects_folder, backup_folder=backup_folder, environment_folders=environment_folders
    )
    for i, zip_file in enumerate(zip_list, 1):
        click.secho(f'{i:3}. {zip_file.name}', fg='green')


# TODO add backup by name. environment-backups backup --name adelantos --upload
