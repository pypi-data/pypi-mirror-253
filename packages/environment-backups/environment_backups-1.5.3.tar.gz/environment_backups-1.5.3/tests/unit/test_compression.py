from pathlib import Path

import pytest

from environment_backups.compression import unzip_file, zip_folder_with_pwd
from environment_backups.exceptions import EnvironmentBackupsError


@pytest.fixture
def create_test_environment(tmp_path):
    # Create a temporary directory with some files
    test_folder = tmp_path / "test_folder"
    test_folder.mkdir()
    (test_folder / "test_file.txt").write_text("This is a test file.")
    return test_folder


@pytest.fixture
def create_zip_path(tmp_path):
    # Create a temporary zip file path
    return tmp_path / "test.zip"


def test_zip_folder_no_password(create_test_environment, create_zip_path):
    zip_folder_with_pwd(create_zip_path, create_test_environment)
    assert create_zip_path.exists()


def test_zip_folder_with_password(create_test_environment, create_zip_path):
    zip_folder_with_pwd(create_zip_path, create_test_environment, password="password123")
    assert create_zip_path.exists()


def test_unzip_folder_no_password(create_test_environment, create_zip_path, tmp_path):
    zip_folder_with_pwd(create_zip_path, create_test_environment)
    unzip_path = tmp_path / "unzip"
    unzip_file(create_zip_path, unzip_path)
    assert (unzip_path / "test_folder" / "test_file.txt").exists()


def test_unzip_folder_with_password(create_test_environment, create_zip_path, tmp_path):
    zip_folder_with_pwd(create_zip_path, create_test_environment, password="password123")
    unzip_path = tmp_path / "unzip"
    unzip_file(create_zip_path, unzip_path, password="password123")
    assert (unzip_path / "test_folder" / "test_file.txt").exists()


def test_zip_nonexistent_folder(create_zip_path):
    nonexistent_folder = Path("/path/does/not/exist")
    with pytest.raises(EnvironmentBackupsError):
        zip_folder_with_pwd(create_zip_path, nonexistent_folder)


def test_unzip_nonexistent_file(tmp_path):
    nonexistent_zip = Path("/path/does/not/exist.zip")
    with pytest.raises(EnvironmentBackupsError):
        unzip_file(nonexistent_zip, tmp_path)
