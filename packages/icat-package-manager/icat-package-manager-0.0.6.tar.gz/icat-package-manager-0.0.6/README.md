# ICAT Package Manager

`icatpackagemanager` is a python package that provides a CLI for automatically downloading and installing ICAT components on a local application server.

## Usage

Invoke the CLI with `python -m icatpackagemanager`, or simply `ipm` if installed with a tool like [pipx](https://github.com/pypa/pipx). Use `-h` or `--help` with any of the commands for full details.

Available commands:

 - `list` - lists all components available from the repo, and which are installed
 - `list <component>` - lists available and installed versions of the component
 - `install <component>`:
   - Checks for installed versions of the component
   - Checks for available versions of the component
   - If there is no newer version, do nothing.
   - Otherwise, download latest distro, and unzips it into install directory
   - If there is no previous version, stop and prompt for configuration
   - Otherwise, copy config from previous version, and (not implemented yet) run the setup script
 - `install <component> <version>` - installs specific version of a package

## Terminology

 - Repository/repo is a website hosting ICAT packages. By default, this is the official `repo.icatproject.org`.
 - A component is one of the ICAT projects ie. `icat.server`, `authn.simple`, etc. Components can have many versions, in the format `x.y.z-<suffix>`.
 - A package is a specific version of a component. Packages are:
   - 'Available' if it exists in the repo
   - 'Installed' if it exists in the install directory
   - 'Deployed' if it's currently running on the application server
 - A distro is a zipfile containing a built package which can be installed
 - The distro cache is a directory containing distros downloaded from the repo
 - The install directory is where distros are unpacked so that they can be deployed

## Planned work

 - Add a `deploy` command or `--deploy` option on `install` to run setup scripts
