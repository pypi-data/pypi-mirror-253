import argparse

from . import commands
from .utils import Version


def run():
    parser = argparse.ArgumentParser(
        description="Find and install ICAT components")
    subparsers = parser.add_subparsers()

    list_parser = subparsers.add_parser(
        "list",
        help="Show available/installed components")
    list_parser.add_argument(
        "component",
        nargs="?",
        help="List available versions of a specific component")
    list_parser.add_argument(
        "-i", "--installed",
        action="store_true",
        dest="installed_only",
        help="Show only installed components, or only installed versions for a "
             "components")
    list_parser.set_defaults(func=commands.do_list)

    install_parser = subparsers.add_parser(
        "install",
        help="Install an ICAT package"
    )
    install_parser.add_argument(
        "component",
        help="The component to install")
    install_parser.add_argument(
        "version",
        help="Specific version to install. Defaults to latest version if not "
             "specified",
        type=Version,
        nargs="?")
    install_parser.add_argument(
        "-s", "--allow-snapshots",
        action="store_true",
        help="Allow snapshot versions. If not set, only non -SNAPSHOT versions "
             "will be used"
    )
    install_parser.set_defaults(func=commands.do_install)

    upgrade_parser = subparsers.add_parser(
        "upgrade",
        help="Upgrade to the newest available version of a component"
    )
    upgrade_parser.add_argument(
        "component",
        help="The component to upgrade")
    upgrade_parser.add_argument(
        "-s", "--allow-snapshots",
        action="store_true",
        help="Allow snapshot versions. If not set, only non -SNAPSHOT versions "
             "will be used"
    )
    upgrade_parser.set_defaults(func=commands.do_upgrade)

    args = parser.parse_args()
    if not hasattr(args, 'func'):
        print("Must provide a subcommand")
        parser.print_usage()
        exit(1)

    kwargs = {
        k: v for k, v in vars(args).items() if k != "func"
    }
    args.func(**kwargs)


if __name__ == "__main__":
    run()
