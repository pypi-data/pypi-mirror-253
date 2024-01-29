import os
import glob
from typing import Optional, List, Union

import fire

from rocket.file_watcher import FileWatcher
from rocket.logger import logger
from rocket.utils import (
    execute_shell_command,
    extract_python_package_dirs,
    extract_python_files_from_folder,
    execute_for_each_multithreaded,
    gather_glob_paths,
)


class Rocket:
    """Entry point of the installed program, all public methods are options of the program"""

    # in seconds
    _interval_repeat_watch: int = 2
    _python_executable: str = "python3"
    _rocket_executable: str = "rocket"

    def setup(self):
        """
        Initialize the application.
        """
        if os.path.exists("setup.py") or os.path.exists(f"pyproject.toml"):
            logger.info("Packaging file already exists so no need to create a new one")
            return

        content = """
import setuptools

setuptools.setup(
    name="myproject",
    version="0.0.1",
    author="",
    author_email="",
    description="",
    url="https://github.com/getyourguide/databricks-rocket",
    packages=setuptools.find_packages(),
)
        """

        with open("setup.py", "a") as myfile:
            myfile.write(content)
        logger.info("Setup.py file created, feel free to modify it with your needs.")

    def launch(
            self,
            project_location: str = ".",
            dbfs_path: Optional[str] = None,
            watch: bool = True,
            glob_path: Optional[Union[str, List[str]]] = None
    ) -> None:
        """
        Entrypoint of the application, triggers a build and deploy
        :param project_location: path to project code, default: `"."`
        :param dbfs_path: path where the wheel will be stored, ex: dbfs:/tmp/myteam/myproject
        :param watch: Set to false if you don't want to automatically sync your files
        :param glob_path: glob string or list of strings for additional files to deploy, e.g. "*.json"
        :return:
        """
        if os.getenv("DATABRICKS_TOKEN") is None:
            raise Exception("DATABRICKS_TOKEN must be set for db-rocket to work")

        if dbfs_path is not None and not dbfs_path.startswith("dbfs:/"):
            raise Exception("`dbfs_path` must start with dbfs:/")

        try:
            execute_shell_command(f"databricks fs ls dbfs:/")
        except Exception as e:
            raise Exception(
                f"Error accessing DBFS via databricks-cli. Please check if your databricks token is set and valid? Try to generate a new token and update existing one with `databricks configure --token`. Error details: {e}"
            )

        if not dbfs_path:
            dbfs_path = f"dbfs:/temp/{os.environ['USER']}"
        if watch:
            project_name = os.path.abspath(project_location).split("/")[-1]
            dbfs_path = f"{dbfs_path}/{project_name}"

        glob_paths = []
        if isinstance(glob_path, str):
            glob_paths = [os.path.join(project_location, glob_path)]
        elif isinstance(glob_path, list):
            glob_paths = [os.path.join(project_location, path) for path in glob_path]

        self._build_and_deploy(watch=watch, project_location=project_location, dbfs_path=dbfs_path, glob_paths=glob_paths)
        if watch:
            watcher = FileWatcher(
                project_location,
                lambda x: self._build_and_deploy(
                    watch=watch,
                    modified_files=watcher.modified_files,
                    dbfs_path=dbfs_path,
                    project_location=project_location,
                    glob_paths=glob_path
                ),
                glob_paths=glob_paths,
            )
            watcher.start()

    def _build_and_deploy(
            self,
            watch: bool,
            project_location: str,
            dbfs_path: str,
            modified_files: Optional[List[str]] = None,
            glob_paths: Optional[List[str]] = None
    ) -> None:
        if modified_files:
            logger.info(f"Found changes in {modified_files}. Overwriting them.")
            self._deploy(
                file_paths=modified_files,
                dbfs_path=dbfs_path,
                project_location=project_location,
            )
            return

        if not watch:
            logger.info(
                "Watch is disabled. Building creating a python wheel from your project"
            )
            wheel_path, wheel_file = self._create_python_project_wheel(project_location)
            self._deploy(
                file_paths=[wheel_path],
                dbfs_path=dbfs_path,
                project_location=os.path.dirname(wheel_path),
            )
            install_path = f'{dbfs_path.replace("dbfs:/", "/dbfs/")}/{wheel_file}'

            dependency_files = ["requirements.in", "requirements.txt"]
            index_urls = []
            for dependency_file in dependency_files:
                dependency_file_path = f"{project_location}/{dependency_file}"
                if os.path.exists(dependency_file_path):
                    with open(dependency_file_path) as f:
                        index_urls = [
                            line.strip()
                            for line in f.readlines()
                            if "index-url" in line
                        ]
            index_urls_options = " ".join(index_urls)
            logger.info(f"""Uploaded wheel to databricks. Install your library in your databricks notebook by running:
%pip install --upgrade pip
%pip install {index_urls_options} {install_path} --force-reinstall""")
            return

        package_dirs = extract_python_package_dirs(project_location)
        files = set()
        for package_dir in package_dirs:
            files.update(extract_python_files_from_folder(package_dir))

        if glob_paths is not None:
            files.update(gather_glob_paths(glob_paths))

        project_files = ["setup.py", "pyproject.toml"]
        for project_file in project_files:
            if os.path.exists(f"{project_location}/{project_file}"):
                files.add(f"{project_location}/{project_file}")

        if os.path.exists(f"{project_location}/pyproject.toml"):
            execute_shell_command(
                "poetry export -f requirements.txt --with-credentials --without-hashes --output requirements.txt"
            )

        dependency_file_exist = False
        dependency_files = ["requirements.in", "requirements.txt"]
        uploaded_dependency_file = ""
        index_urls = []
        for dependency_file in dependency_files:
            dependency_file_path = f"{project_location}/{dependency_file}"
            if os.path.exists(dependency_file_path):
                files.add(dependency_file_path)
                uploaded_dependency_file = dependency_file
                dependency_file_exist = True
                with open(dependency_file_path) as f:
                    index_urls = [
                        line.strip() for line in f.readlines() if "index-url" in line
                    ]
        self._deploy(
            file_paths=list(files), dbfs_path=dbfs_path, project_location=project_location
        )

        install_path = f'{dbfs_path.replace("dbfs:/", "/dbfs/")}'
        index_urls_options = " ".join(index_urls)

        if dependency_file_exist:
            logger.info(
                f"""Watch activated. Uploaded your project to databricks. Install your project in your databricks notebook by running:
%pip install --upgrade pip
%pip install {index_urls_options} -r {install_path}/{uploaded_dependency_file}
%pip install --no-deps -e {install_path}
dbutils.library.restartPython()

and following in a new Python cell:
%load_ext autoreload
%autoreload 2"""
            )
        else:
            logger.info(
                f"""Watch activated. Uploaded your project to databricks. Install your project in your databricks notebook by running:
%pip install --upgrade pip
%pip install -e {install_path}

and following in a new Python cell:
%load_ext autoreload
%autoreload 2"""
            )

    def _deploy(
            self,
            file_paths: List[str],
            dbfs_path: str,
            project_location: str
    ) -> None:
        def helper(file: str) -> None:
            target_path = f"{dbfs_path}/{os.path.relpath(file, project_location)}"
            execute_shell_command(f"databricks fs cp --recursive --overwrite {file} {target_path}")
            logger.info(f"Uploaded {file} to {target_path}")

        execute_for_each_multithreaded(file_paths, lambda x: helper(x))

    def _create_python_project_wheel(self, project_location: str) -> (str, str):
        dist_location = f"{project_location}/dist"
        execute_shell_command(f"rm {dist_location}/* 2>/dev/null || true")

        if os.path.exists(f"{project_location}/setup.py"):
            logger.info("Found setup.py. Building python library")
            execute_shell_command(
                f"cd {project_location} ; {self._python_executable} -m build --outdir {dist_location} 2>/dev/null"
            )
        elif os.path.exists(f"{project_location}/pyproject.toml"):
            logger.info("Found pyproject.toml. Building python library with poetry")
            execute_shell_command(
                f"cd {project_location} ; poetry build --format wheel"
            )
        else:
            raise Exception(
                "To be turned into a library your project has to contain a setup.py or pyproject.toml file"
            )

        wheel_file = execute_shell_command(
            f"cd {dist_location}; ls *.whl 2>/dev/null | head -n 1"
        ).replace("\n", "")
        wheel_path = f"{dist_location}/{wheel_file}"
        return wheel_path, wheel_file


def main():
    fire.Fire(Rocket)
