from importlib.metadata import entry_points
import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# The text of the README file
REQUIRE = (HERE / "requirements.txt").read_text()

__version__ = "0.0.1"

setup(
    name="verup",
    version=__version__,
    url = 'https://github.com/vishalvvr/verup',
    author = 'Vishal Vijayraghavan',
    author_email = 'vishalvvr@fedoraproject.org',
    license = 'GPLv3',
    classifiers = [
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    description = 'Version bumper for any package locally, pypi, github',
    long_description = README,
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"":"src"},
    include_package_data=True,
    install_requires = REQUIRE,
    entry_points={
        "console_scripts":[
            "verup=verup.main:main",
        ]
    },
)
