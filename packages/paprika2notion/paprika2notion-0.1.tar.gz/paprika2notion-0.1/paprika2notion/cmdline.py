from argparse import ArgumentParser
from .command import get_installed_commands, get_config


def main():
    commands = get_installed_commands()
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    subparsers.required = True


