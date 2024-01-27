from typing import Optional

from . import files
from . import repo
from .utils import Version


def _get_component_versions(component: str, installed_only: bool):
    installed_only_packages = files.get_installed_packages()
    installed_only_versions = installed_only_packages.get(component, [])

    if installed_only:
        for v in installed_only_versions:
            yield v
    else:
        available_versions = repo.get_component_versions(component)
        for v in available_versions:
            if v in installed_only_versions:
                yield f"{v} (installed)"
            else:
                yield v


def _get_packages(installed_only: bool):
    installed_only_packages = files.get_installed_packages()

    if installed_only:
        for package in installed_only_packages:
            current = max(installed_only_packages[package])
            yield f"{package} - {current}"
    else:
        available = repo.get_components()
        for package in available:
            if package in installed_only_packages:
                current = max(installed_only_packages[package])
                yield f"{package} (installed: {current})"
            else:
                yield package


def do_list(component: Optional[str], installed_only: bool):
    if component:
        source = _get_component_versions(component, installed_only)
    else:
        source = _get_packages(installed_only)

    for line in source:
        print(line)


def do_install(
        component: str,
        version: Optional[Version] = None,
        allow_snapshots=False):
    installed = files.get_installed_packages().get(component, [])

    if version:
        if version in installed:
            print(f"{component} {version} is already installed")
            return
        install_version = version
    else:
        all_available = repo.get_component_versions(component)
        available = [v for v in all_available if
                     (allow_snapshots or not v.is_snapshot())]
        latest = max(available)
        if latest in installed:
            print(f"Latest available version, {latest}, is already installed")
            if latest != max(all_available):
                print(f"Newer snapshot, {max(all_available)}, is available")
            return
        install_version = latest

    repo.download_distro(component, install_version)
    dest = files.extract_distro(component, install_version)

    if not installed:
        print(
            f"Installed {dest}. No prior version existed, so configuration "
            "must be completed manually")
        return

    print(f"Copying config from existing install to {dest}")
    files.copy_config(component, max(installed), install_version)


def do_upgrade(component: str, allow_snapshots: bool = False):
    installed_versions = files.get_installed_packages().get(component, [])
    if not installed_versions:
        print(f"No existing {component} install to upgrade")
        return
    do_install(component, allow_snapshots=allow_snapshots)
