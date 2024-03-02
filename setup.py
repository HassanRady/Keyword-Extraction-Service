from setuptools import setup, find_packages
from pathlib import Path

# Package meta-data.
NAME = "keywords-extractor"
DESCRIPTION = "A simple spark streaming handler."
URL = "https://github.com/HassanRady/" + NAME
EMAIL = "hassan.khaled.rady@gmail.com"
AUTHOR = "Hassan Rady"
REQUIRES_PYTHON = ">=3.11.0"

ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / "src"
REQUIREMENTS = ROOT_DIR / "requirements.txt"

with open(PACKAGE_DIR / "VERSION") as f:
    VERSION = f.read().strip()

# Long description
with open("README.md") as readme_file:
    readme = readme_file.read()


def list_reqs():
    with open(REQUIREMENTS) as fd:
        return fd.read().splitlines()


setup(
    author=AUTHOR,
    author_email=EMAIL,
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=readme,
    url=URL,
    python_requires=REQUIRES_PYTHON,
    install_requires=list_reqs(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    license="MIT license",
    include_package_data=True,
    packages=find_packages(include=[NAME, NAME + ".*"]),
    test_suite="tests",
    zip_safe=False,
)
