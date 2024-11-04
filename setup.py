from pathlib import Path
# Used for handling filesystem paths in an object-oriented way.

from setuptools import find_packages
# used to automatically discover all Python packages and sub-packages.

from setuptools import setup
# The main function from setuptools used to define metadata and options for the package.
# This code is a Python setup script that uses setuptools to define the configuration
# for packaging and distributing a Python project
package_path = Path(__file__).parent
# package_path holds the path to the directory containing this setup script (setup.py).
# this is the path to the repo directly currently right now !!!!!!!!!!

version_path = Path(__file__).parent.joinpath(f"src/patchcore/VERSION")
# # this is adding the current path to the version path that already exits
# inside it just 0.1.0
version = version_path.read_text().strip()
# eads the contents of the VERSION file and removes any leading or trailing whitespace.
# This ensures the package version is read dynamically from the file.
# you have soemthing inside with this value 0.1.0
install_requires = (
    Path(__file__).parent.joinpath("requirements.txt").read_text().splitlines()
)
# install_requires: Reads and splits the contents of requirements.txt into a list of dependencies.
# These dependencies will be installed automatically when the package is installed.
# this is very intersting
data_files = [
    str(version_path.relative_to(package_path)),
]
# data_files is a list containing the relative path to the VERSION file.
# This means the VERSION file will be included as part of the package when it's distributed.
setup(
    name="patchcore",
    version=version,
    install_requires=install_requires,
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    data_files=data_files,
)
# name: Name of the package (patchcore).
# version: Version number from the VERSION file.
# package_dir={"": "src"}: Specifies that the root package directory is src.
# packages=find_packages("src"): Finds and lists all packages under the src directory.
# Ensures that non-Python files specified in MANIFEST.in are included in the package.