#!/usr/bin/env python
"""clancy.py

Usage:
    clancy.py [-u <user>] create
    clancy.py [-u <user>] delegate --time <time> --usages <usages>
    clancy.py [-u <user>] modify --action <action> --target <target>
    clancy.py [-u <user>] encrypt --owners <owners> --min <minimum> (--str <string> | --file <path>)
    clancy.py [-u <user>] decrypt (--str <string> | --file <path>)
    clancy.py [-u <user>] summary
    clancy.py [-u <user>] password

    clancy.py --help
    clancy.py --version

Options:
    --time <time>      Delegation time string.
    --usages <usages>  Delegation usages.

    --action <action>  Preform action on target. One of: revoke, admin, delete.
    --target <target>  User to modify.

    --owners <owners>  Comma separated list of owners.
    --min <minimum>    Minimum delegations required to decrypt data.
    --str <string>     Base64 encoded string to operate on.
    --file <path>      Path to a file of base64 encoded data to operate on.

    -u, --user <user>  User to log in as. Defaults to current user.
    -h, --help         Show this help message and exit.
    -v, --version      Show version and exit.
"""
from docopt import docopt

VERSION = '0.0.1'

if __name__ == '__main__':
    args = docopt(__doc__, version=VERSION)
    print(args)
