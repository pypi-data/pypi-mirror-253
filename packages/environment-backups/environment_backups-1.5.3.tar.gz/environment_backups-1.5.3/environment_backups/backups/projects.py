import os
from pathlib import Path
from typing import Any, Dict, List


def list_all_projects(projects_folder: Path) -> List[str]:
    """Lists all project directories within a specified folder.

    Args:
        projects_folder (Path): The path to the folder containing projects.

    Returns:
        List[str]: A list of folder paths that represent individual projects.

    """
    folders = [x.path for x in os.scandir(projects_folder) if x.is_dir()]
    return folders


def get_projects_envs(project_folder: Path, environment_folders: List[str]) -> Dict[str, Any]:
    """Gets the environment folders for each project in the specified project folder.

    This function scans each project folder and checks if it contains any of the specified
    environment folders. If so, it adds the project to a dictionary with the environment paths.

    Args:
        project_folder (Path): The path to the folder containing multiple projects.
        environment_folders (List[str]): A list of folder names to look for in each project
                                         folder, representing different environments.

    Returns:
        Dict[str, Any]: A dictionary where each key is a project name and the value is a
                        dictionary containing the path to its environment folders, if any.

    """
    folders = list_all_projects(project_folder)
    folder_dict = dict()
    for folder in folders:
        path = Path(folder)
        for environment_folder in environment_folders:
            envs = path / environment_folder
            if envs.exists():
                folder_dict[path.name] = {'envs': envs}
    return folder_dict
