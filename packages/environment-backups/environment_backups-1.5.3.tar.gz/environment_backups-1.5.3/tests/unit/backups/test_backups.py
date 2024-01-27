import json
from pathlib import Path

import pytest
from freezegun import freeze_time

from environment_backups.backups.backups import backup_environment, backup_envs
from environment_backups.backups.projects import get_projects_envs, list_all_projects
from environment_backups.compression import zip_folder_with_pwd
from environment_backups.exceptions import ConfigurationError
from tests.factories import projects_folder_tree_factory


def test_list_all_projects_with_existing_folders(mocker):
    # Mock os.scandir to return a list of mock directories
    mocker.patch(
        'os.scandir',
        return_value=[mocker.Mock(is_dir=lambda: True, path='dir1'), mocker.Mock(is_dir=lambda: True, path='dir2')],
    )
    assert list_all_projects(Path('/some/path')) == ['dir1', 'dir2']


def test_list_all_projects_with_no_folders(mocker):
    # Mock os.scandir to return an empty list
    mocker.patch('os.scandir', return_value=[])
    assert list_all_projects(Path('/some/empty/path')) == []


def test_get_projects_envs_with_valid_data(mocker):
    # Mock list_all_projects to return specific folders
    mocker.patch('environment_backups.backups.projects.list_all_projects', return_value=['project1', 'project2'])
    # Mock Path.exists to return True
    mocker.patch('pathlib.Path.exists', return_value=True)
    expected_result = {
        'project1': {'envs': Path('project1/env_folder')},
        'project2': {'envs': Path('project2/env_folder')},
    }
    assert get_projects_envs(Path('/projects'), ['env_folder']) == expected_result


def test_get_projects_envs_with_no_projects(mocker):
    mocker.patch('environment_backups.backups.projects.list_all_projects', return_value=[])
    assert get_projects_envs(Path('/projects'), ['env_folder']) == {}


def test_zip_folder_with_pwd_without_password(mocker, tmp_path):
    # Set up a temporary directory and files for zipping
    folder_to_zip = tmp_path / "test_folder"
    folder_to_zip.mkdir()
    (folder_to_zip / "test_file.txt").write_text("test content")

    zip_file = tmp_path / "test.zip"

    # Call the function
    zip_folder_with_pwd(zip_file, folder_to_zip)

    # Check if the zip file was created
    assert zip_file.exists()


def test_zip_folder_with_pwd_with_password(mocker, tmp_path):
    # Similar setup as above, but pass a password to the function
    folder_to_zip = tmp_path / "test_folder"
    folder_to_zip.mkdir()
    (folder_to_zip / "test_file.txt").write_text("test content")

    zip_file = tmp_path / "test.zip"

    zip_folder_with_pwd(zip_file, folder_to_zip, password="secret")

    assert zip_file.exists()


def test_zip_folder_with_empty_directory(mocker, tmp_path):
    # Test with an empty directory
    folder_to_zip = tmp_path / "empty_folder"
    folder_to_zip.mkdir()

    zip_file = tmp_path / "empty.zip"

    zip_folder_with_pwd(zip_file, folder_to_zip)

    assert zip_file.exists()


@freeze_time("2023-11-02 13:16:12")
@pytest.mark.asyncio
async def test_backup_envs_with_valid_data(tmp_path):
    # Mock get_projects_envs to return a dictionary of projects with environments
    projects_folder, _ = projects_folder_tree_factory(root_folder=tmp_path)

    expected_timestamp = '20231102_13'

    # Paths for projects folder and backup folder
    backup_folder = tmp_path / 'backups'
    backup_folder.mkdir()

    # Call the function
    zip_list, b_folder = await backup_envs(
        projects_folder=projects_folder, backup_folder=backup_folder, environment_folders=['.envs'], password=None
    )

    # Assertions
    assert len(zip_list) == 1
    assert b_folder == backup_folder / expected_timestamp
    assert zip_list[0] == backup_folder / expected_timestamp / 'project1.zip'
    assert zip_list[0].exists()


@pytest.mark.asyncio
async def test_backup_environments_with_valid_configuration(tmp_path, fixtures_folder, mocker):
    mock_config_file = fixtures_folder / 'app_configuration.json'
    with open(mock_config_file, 'r') as f:
        config = json.load(f)

    projects_folder, _ = projects_folder_tree_factory(root_folder=tmp_path, projects_folder_name='PycharmProjects')
    backup_folder = tmp_path / 'backups'
    backup_folder.mkdir()
    mock_date = '2012-01-14 13:01:45'
    mock_configuration = {
        "name": "test_env",
        "projects_folder": f"{projects_folder}",
        "backup_folder": f"{backup_folder}",
        "computer_name": "adl-computer",
    }
    config['configurations'].append(mock_configuration)

    mocker.patch(
        'environment_backups.backups.backups.get_configuration_by_name', return_value=(mock_configuration, 100.0)
    )
    # Mock CONFIGURATION_MANAGER and get_configuration_by_name
    mocker.patch("environment_backups.backups.backups.CONFIGURATION_MANAGER.get_current", return_value=config)
    with freeze_time(mock_date):
        zip_list, b_folder = await backup_environment('test_env', use_async=False)

    # Assertions
    assert len(zip_list) == 1
    assert zip_list[0] == backup_folder / '20120114_13_adl-computer' / 'project1.zip'
    assert zip_list[0].exists()
    assert b_folder == backup_folder / '20120114_13_adl-computer'


@pytest.mark.asyncio
async def test_backup_environments_without_computer_name(tmp_path, fixtures_folder, mocker):
    mock_config_file = fixtures_folder / 'app_configuration.json'
    with open(mock_config_file, 'r') as f:
        config = json.load(f)

    projects_folder, _ = projects_folder_tree_factory(root_folder=tmp_path, projects_folder_name='PycharmProjects')
    backup_folder = tmp_path / 'backups'
    backup_folder.mkdir()
    mock_date = '2012-01-14 13:01:45'
    mock_configuration = {
        "name": "test_env",
        "projects_folder": f"{projects_folder}",
        "backup_folder": f"{backup_folder}",
        # "computer_name": "adl-computer",
    }
    config['configurations'].append(mock_configuration)

    mocker.patch(
        'environment_backups.backups.backups.get_configuration_by_name', return_value=(mock_configuration, 100.0)
    )
    # Mock CONFIGURATION_MANAGER and get_configuration_by_name
    mocker.patch("environment_backups.backups.backups.CONFIGURATION_MANAGER.get_current", return_value=config)
    with freeze_time(mock_date):
        zip_list, b_folder = await backup_environment('test_env', use_async=False)

    # Assertions
    assert len(zip_list) == 1
    assert zip_list[0] == backup_folder / '20120114_13' / 'project1.zip'
    assert zip_list[0].exists()
    assert b_folder == backup_folder / '20120114_13'


@pytest.mark.asyncio
async def test_backup_environments_with_invalid_configuration(mocker):
    # Mock CONFIGURATION_MANAGER and get_configuration_by_name to return None
    mocker.patch('environment_backups.backups.backups.get_configuration_by_name', return_value=(None, 100.0))

    # Test with an invalid configuration to raise ConfigurationError
    with pytest.raises(ConfigurationError) as excinfo:
        await backup_environment('invalid_env', use_async=False)
    assert 'No environment configuration found for "invalid_env"' in str(excinfo.value)
