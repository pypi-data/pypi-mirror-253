from pathlib import Path

import pytest

from environment_backups.zipper import zip_folders_with_pwd_async
from tests.factories import projects_folder_tree_factory


@pytest.mark.asyncio
async def test_zip_folders_with_pwd_async(tmp_path):
    projects_folder_tree_factory(root_folder=tmp_path, projects_folder_name='MyProjects')
    # backup_folder = Path().home() / 'Documents'
    backup_folder = tmp_path / 'backups'
    backup_folder.mkdir()

    source_folder = tmp_path / 'MyProjects'

    results = await zip_folders_with_pwd_async(
        source_folder=source_folder, backup_folder=backup_folder, environment_folders=['.envs'], password=None
    )

    zip_file = backup_folder / 'project1.zip'
    assert zip_file.exists()
    assert len(results) == 1
    assert Path(results[0]) == zip_file
