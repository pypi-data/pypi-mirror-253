from typing import List, Dict
import argparse
import sys
import requests

"""
verup
"""

def version_bump(version:str, type:str) -> str:
    """
    i/p: <version str> - eg: 0.1.3
    o/p: <version bump type> (major,minor,patch)
    Read more for semantic versioning https://semver.org/
    """
    # remove v from version string if present
    if version.startswith("v"):
        version = version.replace("v","")
    
    ver_list: List = version.split(".")
    
    ver_template: Dict = {
        "major": int(ver_list[0]),
        "minor": int(ver_list[1]),
        "patch": int(ver_list[2]),
    }

    ver_template[type] += 1
    if type == "major":
        ver_template['minor'], ver_template['patch'] = 0, 0
    elif type == "minor":
        ver_template['patch'] = 0
    
    return f"{ver_template['major']}.{ver_template['minor']}.{ver_template['patch']}"

def main():
    parser = argparse.ArgumentParser(
                    prog='verup',
                    description='version bump program')
    parser.add_argument("-t","--type", choices=['major', 'minor', 'patch'], help="specify what type of semver increment you want")
    parser.add_argument("-n","--package-name",help="specify package name and if its github repo then specify user/repo-name ")
    parser.add_argument("-c","--current-version", help="if you want to version bump locally then specify your current version of the package")
    parser.add_argument("-r","--repo", choices=['pypi', 'testpypi', 'github'], help="if you want to version bump any package which is on pypi or github then use this option")
    args = parser.parse_args()
    
    if not args.type:
        print("input correct version bump type: major/minor/patch in -t flag")
        sys.exit(1)
    
    if args.repo and not args.package_name:
        print("please provide correct package name in -n flag")
        sys.exit(1)
    
    if args.repo and args.package_name:
        
        url = None
        cur_version = None

        if args.repo == "github":
            url = f"https://api.github.com/repos/{args.package_name}/releases/latest"
        else:
            pypi_url=f"https://pypi.org/pypi/{args.package_name}/json"
            testpypi_url=f"https://test.pypi.org/pypi/{args.package_name}/json"
            url = pypi_url if args.repo == "pypi" else testpypi_url
        
        res = requests.get(url).json()
        
        if args.repo == "github":
            cur_version = res['tag_name']
        else:
            cur_version = res['info']['version']
        
        print(version_bump(cur_version, args.type))
        
    else:
        if not args.current_version:
            print("please specify -c flag with current version")
            sys.exit(1)
        print(version_bump(args.current_version, args.type))

if __name__ == "__main__":
    main()
