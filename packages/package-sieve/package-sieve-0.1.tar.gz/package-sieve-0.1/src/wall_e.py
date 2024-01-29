from ast import parse
from typing import Any
from ast import NodeVisitor
from pathlib import Path
from argparse import ArgumentParser
from pkg_resources import get_distribution
from pkg_resources import DistributionNotFound


class ImportCollector(NodeVisitor):
    """
    Extended `NodeVisitor` class to collect imported nodes
    in a given python file.

    `visit_Import` and `visit_ImportFrom` has been overridden
    to check whether the module is standard or third party
    based on the installation location

    """

    def __init__(self):
        self.imports = set()

    def visit_Import(self, node):
        for alias in node.names:
            try:
                if "site-packages" in __import__(alias.name).__file__:
                    self.imports.add(alias.name)
            except ModuleNotFoundError:
                self.imports.add(alias.name)
            except AttributeError:
                pass
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        module = node.module
        for alias in node.names:
            try:
                if "site-packages" in __import__(module).__file__:
                    self.imports.add(module if module else alias.name)
            except ModuleNotFoundError:
                self.imports.add(module if module else alias.name)
            except AttributeError:
                pass
        self.generic_visit(node)


def get_modules_from_file(filename: str) -> set:
    """
    uses `ImportCollector` to analyse and collect third-party modules

    Args:
        filename (str): absolute file path

    Returns:
        set: set of third party module names
    """
    with open(filename, "r") as file:
        node = parse(file.read())
        collector = ImportCollector()
        collector.visit(node)
        return collector.imports


def traverse_directory(base_path: str, exclusions: list) -> set:
    """
    Traverse through all files in the given directory,
    excluding files and folders in exclusions list,
    where exclusions are specified as relative paths.

    :param base_path: Path of the directory to traverse.
    :param exclusions: List of relative file or folder paths to exclude.
    """

    third_party_modules = set()

    base_path = Path(base_path).resolve()
    exclusions = [base_path.joinpath(exclusion).resolve() for exclusion in exclusions]

    for path in base_path.rglob("*"):
        if any(
            exclusion in path.parents or exclusion == path for exclusion in exclusions
        ):
            continue

        if path.is_file() and path.name.endswith(".py"):
            modules = get_modules_from_file(path)
            for module in modules:
                module_name = ""

                # to split module names like "pymysql.cursors"
                if "." in module:
                    module = module.split(".")[0]

                try:
                    package_info = get_distribution(module)
                    module_name = f"{package_info.project_name}=={package_info.version}"
                except DistributionNotFound:
                    # modules like bs4, twocaptcha
                    module_name = f"{module} # 🚨 alert"
                third_party_modules.add(module_name)

    return third_party_modules


def main() -> Any:
    parser = ArgumentParser()
    parser.add_argument(
        "--project_folder", help="Absolute path of the project directory", required=True
    )
    parser.add_argument(
        "--exclude",
        help="Files/Folders to be excluded in comma seperated manner. Eg. venv, __pycache__ etc",
        required=False,
    )
    args = parser.parse_args()

    modules = traverse_directory(args.project_folder, args.exclude.split(","))

    with open("requirements.txt", "w") as _f:
        _f.write("\n".join(modules))


if __name__ == "__main__":
    """
    Known issues:
    1. Modules with different project name and import names are not covered Eg. BeautifulSoup4 @ bs4
    2. Modules which are not used in code will not be covered. Eg. ruff, black
    """
    main()
