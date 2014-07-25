import sys
import getpass
import json


def abort(errstr):
    sys.stderr.write('ERROR: {}\n'.format(errstr))
    sys.exit(1)


def warn(warnstr):
    sys.stderr.write('WARNING: {}\n'.format(warnstr))


def goodquit(exitstr):
    sys.stdout.write('\n{}\n'.format(exitstr))
    sys.exit()


def goodquit_json(jsondata):
    exitstr = json.dumps(jsondata, indent=2, sort_keys=True)
    sys.stdout.write('\nServer Response\n---------------\n')
    sys.stdout.write('{}\n'.format(exitstr))
    sys.exit()


def authenticate(username):
    try:
        sys.stdout.write('\nEnter password\n--------------\n')
        sys.stdout.write('User: {}\n'.format(username))
        password = getpass.getpass()
    except getpass.GetPassWarning:
        abort('Password may be echoed. GTFO.')
        sys.exit(1)
    return password


def encode_b64str():
    try:
        return raw_input('String to encode: ').encode('base64')
    except TypeError:
        abort('Invalid string')


def read_file(fp):
    try:
        with open(fp) as f:
            return f.read()
    except IOError:
        abort("couldn't open file {}".format(fp))
