"""clancy

A command line client for Red October.

Usage:
    clancy create [--user <user> --server <server> --cacert <cacert_path>]
    clancy delegate --time <time> --uses <uses> [--user <user> --server <server> --cacert <cacert_path>]
    clancy encrypt --owners <owners> --min <minimum> (--str <string> | --file <path>) [--user <user> --server <server> --cacert <cacert_path>]
    clancy decrypt (--str <string> | --file <path>) [--user <user> --server <server> --cacert <cacert_path>]
    clancy summary [--user <user> --server <server> --cacert <cacert_path>]
    clancy change-password [--user <user> --server <server> --cacert <cacert_path>]
    clancy modify --action <action> --target <target> [--user <user> --server <server> --cacert <cacert_path>]
    clancy base64-encode

    clancy --help
    clancy --version

Commands:
    create:           Initialize a new vault.
    delegate:         Delegate your password to the server for a fixed time and
                      number of decryptions.
    encrypt:          Allows an admin user to encrypt a piece of data.
    decrypt:          Allows an admin to decrypt a piece of data.
    summary:          Provides a list of users with keys on the system.
    change-password:  Change your password.
    modify:           Modify the state of another user.
    base64-encode     Encode a string for uploading to Red October.

Options:
    --time <time>      Delegation time string. Use Go duration string format.
                       For example: "2h30m"
    --uses <uses>      Delegation use limit. Must be an integer.
    --action <action>  Preform action on target. One of: revoke, admin, delete.
    --target <target>  User to modify.
    --owners <owners>  Comma separated list of owners.
    --min <minimum>    Minimum delegations required to decrypt data. Must be an
                       integer.
    --str <string>     Base64 encoded string.
    --file <path>      Path to a file of base64 encoded data.
    --user <user>      User to log in as. Defaults to current user.
    --server <server>  Red October server.
    --cacert <cacert>  Absolute path to CA cert.
    -h, --help         Show this help message and exit.
    -v, --version      Show version and exit.
"""

__version__ = '0.0.2'

import sys

from docopt import docopt

from .config import load_args
from .utils import authenticate, encode_b64str, goodquit
from .engage import engage


def main():
    try:
        docopt_args = docopt(__doc__, version=__version__)

        # b64 encode takes no args
        if docopt_args['base64-encode']:
            goodquit('Base64\n------\n{}'.format(encode_b64str()))

        args = load_args(docopt_args)
        password = authenticate(args['--user'])
        engage(args, password)
    except KeyboardInterrupt:
        sys.stderr.write('\nOkay, bye\n')
        sys.exit(130)
