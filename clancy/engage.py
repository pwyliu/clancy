import getpass

from .utils import goodquit_json, read_file
from .redoctober import api_call


def engage(args, password):
    """
    Construct payloads and POST to Red October
    """
    if args['create']:
        payload = {'Name': args['--user'], 'Password': password}
        goodquit_json(api_call('create', args, payload))

    elif args['delegate']:
        payload = {
            'Name': args['--user'], 'Password': password,
            'Time': args['--time'], 'Uses': args['--uses']
        }
        goodquit_json(api_call('delegate', args, payload))

    elif args['encrypt']:
        payload = {
            'Name': args['--user'], 'Password': password,
            'Minimum': args['--min'], 'Owners': args['--owners'].split(','),
            'Data': (args['--str'] if args['--file'] is None
                     else read_file(args['--file']))
        }
        goodquit_json(api_call('encrypt', args, payload))

    elif args['decrypt']:
        payload = {
            'Name': args['--user'], 'Password': password,
            'Data': (args['--str'] if args['--file'] is None
                     else read_file(args['--file']))
        }
        goodquit_json(api_call('decrypt', args, payload))

    elif args['summary']:
        payload = {'Name': args['--user'], 'Password': password}
        goodquit_json(api_call('summary', args, payload))

    elif args['change-password']:
        args['newpass'] = getpass.getpass('New Password: ')
        payload = {
            'Name': args['--user'], 'Password': password,
            'NewPassword': args['newpass']
        }
        goodquit_json(api_call('password', args, payload))

    elif args['modify']:
        payload = {
            'Name': args['--user'], 'Password': password,
            'Command': args['--action'], 'ToModify': args['--target']
        }
        goodquit_json(api_call('modify', args, payload))
