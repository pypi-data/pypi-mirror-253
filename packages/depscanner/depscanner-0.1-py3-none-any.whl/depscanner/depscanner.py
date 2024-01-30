#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : nickdecodes
@Email   : nickdecodes@163.com
@Usage   :
@FileName: depscanner.py
@DateTime: 2024/1/29 23:41
@SoftWare: 
"""

import os
import re
from typing import List, Set
from stdlib_list import stdlib_list


class DepScanner:
    @classmethod
    def write_requirements(cls, imports: Set[str], file_path: str = "requirements.txt") -> None:
        """
        Writes the provided set of packages to a requirements.txt file.

        This method takes a set of package names and writes them into a specified file,
        sorted alphabetically. If no filename is specified, 'requirements.txt' is used by default.
        This is commonly used to create a requirements file for Python projects, listing all external packages.

        Args:
            imports (Set[str]): A set of package names to be written to the requirements file.
            file_path (str, optional): The name of the file to write the requirements to. Defaults to "requirements.txt".

        Returns:
            None
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            for imp in sorted(imports):
                file.write(imp + '\n')
        print(f"Requirements written to {file_path}")

    @classmethod
    def find_python_files(cls, directory: str) -> List[str]:
        """
        Recursively find all Python files (.py) in the given directory.

        Args:
            directory (str): The directory path to search in.

        Returns:
            List[str]: A list of paths to Python files found within the directory.
        """
        py_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    py_files.append(os.path.join(root, file))
        return py_files

    @classmethod
    def extract_imports(cls, file_path: str, python_version: str) -> Set[str]:
        """
        Extracts import statements from a specified Python file and filters out packages that are part of the
        Python standard library. Only considers lines where 'from' or 'import' are at the beginning.

        Args:
            file_path (str): The path to the Python file to analyze.
            python_version (str): The target Python version used to determine which packages are part of the standard
                                  library.

        Returns:
            Set[str]: A set of non-standard library package names extracted from the file.
        """
        imports = set()
        stdlib_modules = set(stdlib_list(python_version))  # Get the standard library list for the specified Python version

        # Adjusted regex to match 'import module' and 'from module import something' forms at the start of a line
        pattern = re.compile(r'^\s*(from\s+(\S+)|import\s+((?:\S+\s*,\s*)*\S+))')

        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                match = pattern.search(line)
                if match:
                    # Extract module names
                    module = match.group(2) or match.group(3)
                    if module:
                        module_names = module.replace(' ', '').split(',')
                        for name in module_names:
                            # Take the root name of the module and check if it's not in the standard library
                            root_module = name.split('.')[0]
                            if root_module not in stdlib_modules:
                                imports.add(root_module)
        return imports

    @classmethod
    def is_project_package(cls, package, project_directory):
        """检查一个包是否是项目内的自定义包"""
        package_path = os.path.join(project_directory, package)
        return os.path.exists(package_path)

    @classmethod
    def scan_project(cls, project_directory, python_version="3.8"):
        """扫描项目目录，提取所有非内置依赖，并写入requirements.txt"""
        py_files = cls.find_python_files(project_directory)
        all_imports = set()
        for file in py_files:
            file_imports = cls.extract_imports(file, python_version)
            all_imports.update(file_imports)

        cls.write_requirements(all_imports)


if __name__ == "__main__":
    project_directory = input("Enter the path to your project directory: ")
    python_version = input("Enter your Python version (e.g., 3.8): ")
    DepScanner.scan_project(project_directory, python_version)

