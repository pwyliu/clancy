import json
from socket import timeout as socket_timeout

import requests

from .utils import abort, warn


def api_call(endpoint, args, payload):
    """
    Generic function to call the RO API
    """
    headers = {'content-type': 'application/json; ; charset=utf-8'}
    url = 'https://{}/{}'.format(args['--server'], endpoint)
    attempt = 0
    resp = None

    while True:
        try:
            attempt += 1
            resp = requests.post(
                url, data=json.dumps(payload), headers=headers,
                verify=args['--cacert']
            )
            resp.raise_for_status()
            break
        except (socket_timeout, requests.Timeout,
                requests.ConnectionError, requests.URLRequired) as ex:
            abort('{}'.format(ex))
        except requests.HTTPError as ex:
            warn('Requests HTTP error: {}'.format(ex))
            if attempt >= 5:
                abort('Too many HTTP errors.')
    if resp is not None:
        try:
            return resp.json()
        except ValueError:
            abort('Unexpected response from server:\n\n{}'.format(resp.text))
    else:
        abort("Couldn't POST to Red October")
