# !/usr/bin/env python3

__version__="0.0.4"

import argparse
import urllib.request
from os.path import basename

def clone_file(url):
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
        filename = basename(url)
        with open(filename, 'wb') as file:
            file.write(content)
        print(f"File cloned successfully and saved as '{filename}' in the current directory.")
    except Exception as e:
        print(f"Error: {e}")

def __main__():
    parser = argparse.ArgumentParser(description="Execute different functions based on command-line arguments.")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)

    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand", help="Choose a subcommand")

    # Subparser for the 'clone + URL' command
    clone_parser = subparsers.add_parser('clone', help='Download a GGUF file/model from URL')
    clone_parser.add_argument('url', type=str, help='URL to download from')

    # Subparser for the 'menu/cpp/c/gpp/g' command
    subparsers.add_parser('menu', help='Connector selection list')
    subparsers.add_parser('cpp', help='cpp connector')
    subparsers.add_parser('c', help='c connector')
    subparsers.add_parser('gpp', help='gpp connector')
    subparsers.add_parser('g', help='g connector')

    args = parser.parse_args()

    if args.subcommand == 'clone':
        clone_file(args.url)
    elif args.subcommand == 'menu':
        from gguf_connector import menu
    elif args.subcommand == 'cpp':
        from gguf_connector import cpp
    elif args.subcommand == 'c':
        from gguf_connector import c
    elif args.subcommand == 'gpp':
        from gguf_connector import gpp
    elif args.subcommand == 'g':
        from gguf_connector import g
