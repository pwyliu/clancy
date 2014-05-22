#!/usr/bin/env python
"""clancy.py

Usage:
    clancy.py create 
    clancy.py delegate --time <time> --usages <usages> 
    clancy.py encrypt --owners <owners> --min <minimum> (--str <string> | --file <path>) 
    clancy.py decrypt (--str <string> | --file <path>) 
    clancy.py summary 
    clancy.py password 
    clancy.py modify --action <action> --target <target> 

    clancy.py --help
    clancy.py --version

Commands:
    create:    Create a new vault.
    delegate:  Delegate your password to the server for a fixed time and number
               of decryptions.
    encrypt:   Allows an admin user to encrypt a piece of data.
    decrypt:   Allows an admin to decrypt a piece of data.
    summary:   Provides a list of users with keys on the system.
    password:  Change your password.
    modify:    Modify the state of another user.

Options:
    --time <time>      Delegation time string.
    --usages <usages>  Delegation usages.

    --action <action>  Preform action on target. One of: revoke, admin, delete.
    --target <target>  User to modify.

    --owners <owners>  Comma separated list of owners.
    --min <minimum>    Minimum delegations required to decrypt data.
    --str <string>     Base64 encoded string to operate on.
    --file <path>      Path to a file of base64 encoded data to operate on.

    -h, --help         Show this help message and exit.
    -v, --version      Show version and exit.
"""
from docopt import docopt
import os
import sys
import getpass
import json
import requests 


def load_args():
    config = {}
    locations = [os.curdir, os.path.expanduser("~/.clancy"), "/etc/clancy"]
    for loc in locations:
        try:
            with open(os.path.join(loc, "clancy.conf"), 'rb') as source:
                config = json.load(source)
                break
        except IOError:
            pass
    return config


def call_server(endpoint, payload):
    pass


VERSION = '0.0.1'
if __name__ == '__main__':
    cli_args = docopt(__doc__, version=VERSION)

    # conf file args take precedence over cli args
    args = dict(cli_args.items() + load_args().items())
    if 'server' not in args:
        sys.stderr.write('No server defined in config file. See Readme.')
        sys.exit(1)
    if 'user' not in args:
        args['user'] = getpass.getuser()

    if args['create']:



