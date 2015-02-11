"""
homeslice.cli
~~~~~~~~~~~~~

This is the CLI for homeslice
"""
from __future__ import print_function

from docopt import docopt

USAGE = """Homeslice.

Usage:
    homeslice init
    homeslice add <repo>
    homeslice install
    homeslice pull

Options:
    -h --help       Show this help message.
    -v --verbose    Output verbose messages.
"""

def main():
    arguments = docopt(USAGE, version="TODO: versioneer")
    print(arguments)


if __name__ == '__main__':
    main()



