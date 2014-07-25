import os

import kaptan
from yaml.parser import ParserError, ScannerError
from schema import Schema, Use, And, SchemaError, Optional

from .utils import abort, warn


def merge(dict_1, dict_2):
    """
    Merge two dictionaries. Values that evaluate to true take priority over
    falsy values. `dict_1` takes priority over `dict_2`.

    https://github.com/docopt/docopt/blob/
    5112ecc663a18a0b25c361b2a30c55b64311d285/examples/
    config_file_example.py#L53
    """
    return dict((str(key), dict_1.get(key) or dict_2.get(key))
                for key in set(dict_2) | set(dict_1))


def validate(args):
    """
    Validate args
    """
    provided = {key: val for key, val in args.iteritems() if val is not None}
    schema = Schema({
        '--user': And(str, len, Use(str.lower)),
        '--server': And(str, len, Use(str.lower)),
        '--cacert': os.path.isfile,
        # ops
        Optional('create'): Use(bool),
        Optional('delegate'): Use(bool),
        Optional('encrypt'): Use(bool),
        Optional('decrypt'): Use(bool),
        Optional('summary'): Use(bool),
        Optional('change-password'): Use(bool),
        Optional('modify'): Use(bool),
        Optional('base64-encode'): Use(bool),
        # delegate params
        Optional('--time'): And(str, len),
        Optional('--uses'): Use(int),
        # encrypt/decrypt params
        Optional('--owners'): And(str, len, Use(str.lower)),
        Optional('--min'): Use(int),
        Optional('--str'): And(str, len),
        Optional('--file'): os.path.isfile,
        # modify params
        Optional('--action'): And(str, len, Use(str.lower)),
        Optional('--target'): And(str, len, Use(str.lower)),
    })
    try:
        return merge(schema.validate(provided), args)
    except SchemaError as ex:
        abort("Missing, invalid or unexpected argument.\n{}".format(ex.message))


def load_args(args):
    """
    Load a config file. Merges CLI args and validates.
    """
    config = kaptan.Kaptan(handler='yaml')
    conf_parent = os.path.expanduser('~')
    conf_app = '.clancy'
    conf_filename = 'config.yaml'

    conf_dir = os.path.join(conf_parent, conf_app)
    for loc in [os.curdir, conf_dir]:
        configpath = os.path.join(loc, conf_filename)
        try:
            if os.path.isfile(configpath):
                config.import_config(configpath)
                break
        except (ValueError, ParserError, ScannerError):
            warn("Ignoring invalid valid yaml file {}".format(configpath))

    config = (config.configuration_data
              if config.configuration_data is not None else {})

    # Prepend '--' to conf file keys so it matches docopt. This is the dumbest
    # thing in the world.
    for key, val in config.items():
        config['--'+key] = val
        del config[key]

    return validate(merge(args, config))
