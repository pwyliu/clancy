#!/usr/bin/env python
"""clancy.py

Usage:
    clancy.py create [--user <user> --server <server> --cacert <cacert_path>]
    clancy.py delegate --time <time> --uses <uses> [--user <user> --server <server> --cacert <cacert_path>]
    clancy.py encrypt --owners <owners> --min <minimum> (--str <string> | --file <path>) [--user <user> --server <server> --cacert <cacert_path>]
    clancy.py decrypt (--str <string> | --file <path>) [--user <user> --server <server> --cacert <cacert_path>]
    clancy.py summary [--user <user> --server <server> --cacert <cacert_path>]
    clancy.py change-password [--user <user> --server <server> --cacert <cacert_path>]
    clancy.py modify --action <action> --target <target> [--user <user> --server <server> --cacert <cacert_path>]

    clancy.py --help
    clancy.py --version

Commands:
    create:           Create a new vault.
    delegate:         Delegate your password to the server for a fixed time and number
                      of decryptions.
    encrypt:          Allows an admin user to encrypt a piece of data.
    decrypt:          Allows an admin to decrypt a piece of data.
    summary:          Provides a list of users with keys on the system.
    change-password:  Change your password.
    modify:           Modify the state of another user.

Options:
    --time <time>      Delegation time string.
    --uses <uses>      Delegation usages.

    --action <action>  Preform action on target. One of: revoke, admin, delete.
    --target <target>  User to modify.

    --owners <owners>  Comma separated list of owners.
    --min <minimum>    Minimum delegations required to decrypt data.
    --str <string>     Base64 encoded string to operate on.
    --file <path>      Path to a file of base64 encoded data to operate on.

    --user <user>      User to log in as.
    --server <server>  Red October server.
    --cacert <cacert>  Absolute path to CA cert.


    -h, --help         Show this help message and exit.
    -v, --version      Show version and exit.
"""
from docopt import docopt
from socket import timeout as socket_timeout
import os
import sys
import getpass
import json
import requests 

# Version string
VERSION = '0.0.1'


def abort(errstr):
    sys.stderr.write('{}\n'.format(errstr))
    sys.exit(1)


def goodquit(exitstr):
    sys.stdout.write('{}\n'.format(exitstr))
    sys.exit()


def goodquit_json(jsondata):
    exitstr = json.dumps(jsondata, indent=2, sort_keys=True)
    sys.stdout.write('\nServer Response\n---------------\n')
    sys.stdout.write('{}\n\n'.format(exitstr))
    sys.exit()


def authenticate(username):
    try:
        sys.stdout.write('\nAuthenticate\n------------\n')
        sys.stdout.write('User: {}\n'.format(username))
        password = getpass.getpass()
    except getpass.GetPassWarning:
        abort('ERROR: Password may be echoed. GTFO.')
        sys.exit(1)
    return password


def load_args():
    config = None
    locations = [os.curdir, os.path.expanduser("~/.clancy"), "/etc/clancy"]
    for loc in locations:
        try:
            with open(os.path.join(loc, "clancy.conf"), 'rb') as source:
                config = json.load(source)
                break
        except IOError:
            pass
        except ValueError:
            abort('ERROR: Config file not valid json.')
    if config is None:
        abort('ERROR: No config file found.')
    return config


def api_call(endpoint, params, payload):
    headers = {'content-type': 'application/json'}
    url = 'https://{}/{}'.format(params['--server'], endpoint)
    attempt = 0
    resp = None
    while True:
        try:
            attempt += 1
            resp = requests.post(
                url, data=payload, headers=headers, verify=args['--cacert']
            )
            resp.raise_for_status()
            break
        except (socket_timeout,
                requests.Timeout,
                requests.ConnectionError,
                requests.URLRequired) as ex:
            abort('ERROR: {}'.format(ex))
        except requests.HTTPError as ex:
            sys.stderr.write('HTTP ERROR: {}'.format(ex))
            if attempt >= 3:
                abort('ERROR: Too many HTTP errors.')
    if resp is not None:
        try:
            return resp.json()
        except ValueError:
            abort('ERROR: unexpected response from server')
    else:
        abort('ERROR: post error')


if __name__ == '__main__':
    try:
        # cli params > config file
        cli_args = docopt(__doc__, version=VERSION)
        conf_args = load_args()
        args = dict(conf_args.items() + cli_args.items())

        # sanity checks
        if cli_args['--user'] is None:
            if u'--user' in conf_args:
                args['--user'] = conf_args['--user']
            else:
                args['--user'] = getpass.getuser()

        if cli_args['--server'] is None:
            if u'--server' in conf_args:
                args['--server'] = conf_args['--server']
            else:
                abort('ERROR: Server not defined. Pass in as parameter or '
                      'define in config file. See README for details.')

        if cli_args['--cacert'] is None:
            if u'--cacert' in conf_args:
                args['--cacert'] = conf_args['--cacert']
            else:
                abort('ERROR: CA cert path not defined. Pass in as parameter '
                      'or define in config file. See README for details.')
        if not os.path.isfile(args['--cacert']):
            abort('ERROR: CA file not found.')

        # get password
        args['--password'] = authenticate(args['--user'])

        # do stuff
        if args['create']:
            upload = json.dumps({
                'Name': args['--user'],
                'Password': args['--password'],
            })
            goodquit_json(api_call('create', args, upload))

        elif args['delegate']:
            upload = json.dumps({
                'Name': args['--user'],
                'Password': args['--password'],
                'Time': args['--time'],
                'Uses': int(args['--uses']),
            })
            goodquit_json(api_call('delegate', args, upload))

        elif args['encrypt']:
            if args['--file']:
                abort('ERROR: not implemented.')
            else:
                enc_data = args['--str']

            upload = json.dumps({
                'Name': args['--user'],
                'Password': args['--password'],
                'Minimum': int(args['--min']),
                'Owners': args['--owners'].split(','),
                'Data': enc_data,
            })
            goodquit_json(api_call('encrypt', args, upload))

        elif args['decrypt']:
            if args['--file']:
                abort('ERROR: not implemented.')
            else:
                dec_data = args['--str']

            upload = json.dumps({
                'Name': args['--user'],
                'Password': args['--password'],
                'Data': dec_data,
            })
            goodquit_json(api_call('decrypt', args, upload))

        elif args['summary']:
            upload = json.dumps({
                'Name': args['--user'],
                'Password': args['--password'],
            })
            goodquit_json(api_call('summary', args, upload))

        elif args['change-password']:
            args['newpass'] = getpass.getpass('New Password: ')
            upload = json.dumps({
                'Name': args['--user'],
                'Password': args['--password'],
                'NewPassword': args['newpass'],
            })
            goodquit_json(api_call('password', args, upload))

        elif args['modify']:
            upload = json.dumps({
                'Name': args['--user'],
                'Password': args['--password'],
                'Command': args['--action'],
                'ToModify': args['--target'],
            })
            goodquit_json(api_call('modify', args, upload))

    except KeyboardInterrupt:
        sys.stderr.write('okay bye\n')
        sys.exit(130)
