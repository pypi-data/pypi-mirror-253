# verup

Its a simple script to bump any package version.
You have local package or package on pypi or on github

use verup and specify version increment type major, minor, patch  

## Setup

```console
> pip install verup
```

## Usage

```console
> verup --help
usage: verup [-h] [-t {major,minor,patch}] [-n PACKAGE_NAME] [-c CURRENT_VERSION] [-r {pypi,testpypi,github}]

version bump program

options:
  -h, --help            show this help message and exit
  -t {major,minor,patch}, --type {major,minor,patch}
                        specify what type of semver increment you want
  -n PACKAGE_NAME, --package-name PACKAGE_NAME
                        specify package name and if its github repo then specify user/repo-name
  -c CURRENT_VERSION, --current-version CURRENT_VERSION
                        if you want to version bump locally then specify your current version of the package
  -r {pypi,testpypi,github}, --repo {pypi,testpypi,github}
                        if you want to version bump any package which is on pypi or github then use this option
```

Happy Coding :)