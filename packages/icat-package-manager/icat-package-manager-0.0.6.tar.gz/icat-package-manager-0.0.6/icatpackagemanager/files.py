import shutil
from pathlib import Path
from typing import List, Dict
from zipfile import ZipFile

from .utils import Version

_default_install_location = Path.home() / "install"
_default_cache_location = Path.home() / ".ipm" / "cache"

Path.mkdir(_default_cache_location, parents=True, exist_ok=True)
Path.mkdir(_default_install_location, parents=True, exist_ok=True)


def get_distro_name(component: str, version: Version) -> str:
    return f"{component}-{version}-distro.zip"


def get_cache_destination(file):
    return _default_cache_location / file


def _get_install_dir(component: str, version: Version) -> Path:
    return _default_install_location / component / str(version)


def extract_distro(component: str, version: Version) -> Path:
    fname = get_distro_name(component, version)
    dest = _get_install_dir(component, version)
    with ZipFile(get_cache_destination(fname), "r") as zf:
        zf.extractall(_default_install_location / component)
        shutil.move(
            _default_install_location / component / component,
            dest)
    return dest


def get_installed_packages(
        d=_default_install_location) -> Dict[str, List[Version]]:
    installed_components = [c for c in d.iterdir() if c.is_dir()]
    return {
        c.name: [Version(v.name) for v in c.iterdir() if Version.is_valid(v.name)]
        for c in installed_components
    }


if __name__ == "__main__":
    print(get_installed_packages())


def copy_config(
        component: str,
        src: Version,
        dest: Version):
    """Copy .properties and .xml files from one installed package to another"""

    src_dir = _get_install_dir(component, src)
    dest_dir = _get_install_dir(component, dest)

    for f in src_dir.glob("*.properties"):
        shutil.copy(f, dest_dir)

    for f in src_dir.glob("*.xml"):
        shutil.copy(f, dest_dir)


if __name__ == "__main__":
    copy_config("icat.server", Version("5.0.1"), Version("6.0.0"))
