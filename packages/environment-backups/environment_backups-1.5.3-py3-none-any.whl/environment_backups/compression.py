import os
from pathlib import Path

from deprecated import deprecated
from pyzipper import WZ_AES, ZIP_DEFLATED, AESZipFile

from environment_backups.exceptions import EnvironmentBackupsError


@deprecated(reason='Use zipper.zip_folder_with_pwd_async')
def zip_folder_with_pwd(zip_file: Path, folder_to_zip: Path, password: str = None) -> None:
    """
    Compresses a folder and creates a zip file with optional password protection.
    @param zip_file: Zip file path
    @param folder_to_zip: Folder to zip
    @param password: Password for the  zip file
    """
    if not folder_to_zip.exists():
        message = f'The target folder to put the zip file {folder_to_zip}does not exist.'
        raise EnvironmentBackupsError(message)

    def zipdir(path: Path, ziph):
        """
        Recursively adds files and directories to a zip file.
        """
        try:
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    ziph.write(file_path, os.path.relpath(file_path, path.parent))
        except ValueError as e:
            error_message = f'Error zipping {path}. Error: {e}'
            raise EnvironmentBackupsError(error_message)

    encryption = WZ_AES if password else None

    with AESZipFile(zip_file, 'w', compression=ZIP_DEFLATED, encryption=encryption, strict_timestamps=False) as zf:
        if password:
            pwd = password.encode('utf-8')
            zf.setpassword(pwd)
        zipdir(folder_to_zip, zf)


def unzip_file(zip_file: Path, destination_folder: Path, password: str = None):
    """
    Extracts a zip file into a specified destination folder, with optional password decryption.
    @param zip_file: Path to the zip file.
    @param destination_folder: Path to the destination folder.
    @param password: Optional password for encrypted zip files.
    """
    if not zip_file.exists() or not zip_file.is_file():
        raise EnvironmentBackupsError(f"The zip file {zip_file} does not exist or is not a file.")

    if not destination_folder.exists():
        os.makedirs(destination_folder)

    with AESZipFile(zip_file, 'r') as zf:
        if password:
            zf.setpassword(password.encode('utf-8'))
        zf.extractall(destination_folder)
