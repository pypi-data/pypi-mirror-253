import shutil
from pathlib import Path
from typing import List, Generator
from urllib.request import urlopen

import lxml.html

from .files import get_cache_destination, get_distro_name
from .utils import Version

_default_repo = "https://repo.icatproject.org/repo/org/icatproject"


def _extract_content_list_from_table(page: str) -> Generator[str, None, None]:
    parsed = lxml.html.fromstring(page)
    table_rows = parsed.xpath("body/table//tr")
    # First rows are headers/dividers, last is a divider
    content_rows = table_rows[3:-1]
    # Second column contains a link element, whose href is what we want
    links = (r.getchildren()[1].getchildren()[0] for r in content_rows)
    return (l.get("href").strip("/") for l in links)


def get_components(repo_url=_default_repo) -> List[str]:
    with urlopen(repo_url) as f:
        if f.status != 200:
            raise Exception(f"Couldn't reach {repo_url}")
        page = f.read().decode()
        return list(_extract_content_list_from_table(page))


def get_component_versions(
        component: str,
        repo_url=_default_repo) -> List[Version]:
    with urlopen(f"{repo_url}/{component}") as f:
        if f.status != 200:
            raise Exception(f"Couldn't reach {repo_url}")
        page = f.read().decode()
        version_strings = _extract_content_list_from_table(page)
        return [Version(v) for v in version_strings if Version.is_valid(v)]


def get_distros(
        component: str,
        version: Version,
        repo_url=_default_repo) -> List[str]:
    with urlopen(f"{repo_url}/{component}/{version}") as f:
        if f.status != 200:
            raise Exception(f"Couldn't reach {repo_url}")
        page = f.read().decode()
        return [f for f in _extract_content_list_from_table(page)
                if f.endswith("distro.zip")]


def download_distro(
        component: str,
        version: Version,
        repo_url=_default_repo) -> Path:

    fname = get_distro_name(component, version)
    if not version.is_snapshot():
        url = f"{repo_url}/{component}/{version}/{fname}"
        print(f"Getting {url}")
    else:
        distro = get_distros(component, version)[-1]
        url = f"{repo_url}/{component}/{version}/{distro}"

    dest = get_cache_destination(fname)

    with urlopen(url) as response, open(dest, "wb") as f:
        if response.status != 200:
            raise Exception(f"Couldn't reach {repo_url}")
        shutil.copyfileobj(response, f)
    return dest


if __name__ == "__main__":
    from pprint import pprint

    pprint(download_distro("icat.server", Version("6.1.0-SNAPSHOT")))
