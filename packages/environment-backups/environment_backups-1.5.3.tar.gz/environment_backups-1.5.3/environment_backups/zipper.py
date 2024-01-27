import asyncio
import os
import shutil
from pathlib import Path
from typing import List

import click
import pyzipper
from rich.progress import Progress

from environment_backups.backups.projects import list_all_projects
from environment_backups.compression import zip_folder_with_pwd


async def zip_folder_with_pwd_async(folder: Path, zip_file: Path, password: str = None):
    """
    Asynchronously compresses a single folder into a zip file with optional password protection.
    """
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, sync_zip_folder_with_pwd, folder, zip_file, password)


def sync_zip_folder_with_pwd(folder: Path, zip_file: Path, password: str = None):
    """
    Synchronously compresses a single folder into a zip file with optional password protection.
    """
    with pyzipper.AESZipFile(zip_file, 'w', compression=pyzipper.ZIP_DEFLATED, strict_timestamps=False) as zipf:
        if password:
            zipf.setpassword(password.encode('utf-8'))
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_path = Path(root) / file
                zipf.write(file_path, file_path.relative_to(folder.parent))


async def zip_folders_with_pwd_async(
    source_folder: Path, backup_folder: Path, environment_folders: List[str], password: str = None
) -> List[Path]:
    zipping_tasks = []
    zipped_files = []
    folders_to_search = [folder for folder in source_folder.iterdir()]

    total_folders = len(folders_to_search)
    # print(f"Found {total_folders}")
    with Progress() as progress_bar:
        task2 = progress_bar.add_task("[green]Processing...", total=100.0)
        for i, item in enumerate(folders_to_search, 1):
            # print(item)
            if item.is_dir():
                # FIXME Support more than one environment folder
                env_folder = item / environment_folders[0]
                if env_folder.exists():
                    zip_file_path = backup_folder / f"{item.name}.zip"
                    # print(f'Zipping {item.name} to {zip_file_path} <<')
                    zipping_tasks.append(zip_folder_with_pwd_async(env_folder, zip_file_path, password))
                    zipped_files.append(zip_file_path)
            advance_percentage = 100.00 / total_folders
            # print(advance_percentage)
            progress_bar.update(task2, advance=advance_percentage)
            # await asyncio.sleep(1.0)

    await asyncio.gather(*zipping_tasks)
    return zipped_files


def main_sync(source: Path, backup: Path, password: str = None):
    projects = list_all_projects(source)

    for project in projects:
        project_path = Path(project)
        zip_file = backup / f'{project_path.name}.zip'
        folder_to_zip = source / f'{project}'
        print(f'Zipping {folder_to_zip} to {zip_file}')
        zip_folder_with_pwd(zip_file=zip_file, folder_to_zip=folder_to_zip)


async def main_async(source: Path, backup: Path, password: str = None):
    zipped_files = await zip_folders_with_pwd_async(source, backup, ['.envs'], password)
    print("Zipped files:", zipped_files)


def clean_and_create_folder(folder: Path):
    if folder.exists():
        shutil.rmtree(folder)
        folder.mkdir()
    else:
        folder.mkdir()


def list_folder_contents(folder: Path):
    i = 0
    for entry in folder.iterdir():
        size = entry.stat().st_size / 1024 / 1024
        i += 1
        print(f'{i} {entry.name:35} exists {entry.exists()} {size :,.2f} MB')
    if i == 0:
        print('No folder found')


if __name__ == '__main__':
    import time

    do_sync = False
    do_async = not do_sync

    source_folder_m = Path.home() / 'Documents' / 'MyProjectsForTests'
    backup_folder_m = Path.home() / 'Documents' / '__zipping_test'

    clean_and_create_folder(backup_folder_m)

    if do_async:
        click.secho(f'Doing asynchronous backups...', fg='cyan')
        # 66.15 se  11.68 s faster 17.66% faster on Dell
        start = time.time()
        asyncio.run(main_async(source_folder_m, backup_folder_m))
        print(f'Async time elapsed: {(time.time() - start):.2f} seconds.')
        list_folder_contents(backup_folder_m)

    if do_sync:
        click.secho(f'Doing synchronous backups', fg='cyan')
        clean_and_create_folder(backup_folder_m)
        # 77.83 s on Dell
        start = time.time()
        main_sync(source_folder_m, backup_folder_m)
        elapsed = time.time() - start
        print(f"Sync time elapsed: {elapsed:.2f} seconds")
        list_folder_contents(backup_folder_m)
