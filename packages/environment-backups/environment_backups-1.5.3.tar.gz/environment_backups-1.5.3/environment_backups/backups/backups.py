import logging
from datetime import datetime
from pathlib import Path
from typing import List, Tuple

from .. import CONFIGURATION_MANAGER
from ..compression import zip_folder_with_pwd
from ..config.configuration import get_configuration_by_name
from ..exceptions import ConfigurationError
from ..zipper import zip_folders_with_pwd_async
from .projects import get_projects_envs

logger = logging.getLogger()


async def backup_envs(
    *,
    projects_folder: Path,
    backup_folder: Path,
    environment_folders: List[str],
    computer_name: str = None,
    password: str = None,
    date_format='%Y%m%d_%H', # FIXME use environment_backups/constants.py:5
    use_async: bool = False,
) -> Tuple[List[Path], Path]:
    project_envs_dict = get_projects_envs(projects_folder, environment_folders)
    timestamp = datetime.now().strftime(date_format)
    if computer_name is None:
        b_folder = backup_folder / timestamp
    else:
        b_folder = backup_folder / f'{timestamp}_{computer_name}'
    b_folder.mkdir(exist_ok=True)

    zip_list = []
    if use_async:
        # FIXME Only use async
        zipped_files = await zip_folders_with_pwd_async(
            source_folder=projects_folder, backup_folder=b_folder, environment_folders=['.envs'], password=password
        )
        return zipped_files, b_folder
    else:
        for project, v in project_envs_dict.items():
            zip_file = b_folder / f'{project}.zip'
            zip_folder_with_pwd(zip_file, v['envs'], password=password)
            zip_list.append(zip_file)
        return zip_list, b_folder


async def backup_environment(environment_name: str, use_async: bool) -> Tuple[List[Path], Path]:
    app_configuration = CONFIGURATION_MANAGER.get_current()
    cfg, _ = get_configuration_by_name(environment_name, app_configuration)
    if cfg is None:
        error_message = f'No environment configuration found for "{environment_name}"'
        raise ConfigurationError(error_message)
    pwd = app_configuration.get('password')
    environment_folders = app_configuration['application'].get('environment_folder_pattern')
    date_format = app_configuration['application'].get('date_format')
    project_folder = Path(cfg['projects_folder'])
    backup_folder = Path(cfg['backup_folder'])
    computer_name = cfg.get('computer_name')

    zip_list, b_folder = await backup_envs(
        projects_folder=project_folder,
        backup_folder=backup_folder,
        environment_folders=environment_folders,
        computer_name=computer_name,
        password=pwd,
        date_format=date_format,
        use_async=use_async,
    )
    return zip_list, b_folder
