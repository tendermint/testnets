#!/usr/bin/env python3

import datetime
import json
import pathlib

import fire
import toml


config_template = """# https://github.com/toml-lang/toml

proxy_app = "tcp://127.0.0.1:{app}"
moniker = "{name}"
fast_sync = true

db_backend = "leveldb"
log_level = "state:info,*:error"

[rpc]
laddr = "tcp://0.0.0.0:{rpc}"

[consensus]
create_empty_blocks_interval = 60

[tx_index]
index_all_tags = true

[p2p]
max_num_peers = 300
pex = true
laddr = "tcp://0.0.0.0:{p2p}"
# validators: {csv_validator_names}
seeds = "{csv_p2p_endpoints}"
"""

default_ports = {
    'p2p': 46656,
    'rpc': 46657,
    'app': 46658,
}


def main(chain_name, for_validator=None, subdir='gaia', skip_sig_checks=True):
    """Specify validator "name" from one of the genesis inclusion requests
    to create a customized config file."""

    if not skip_sig_checks:
        # idea is for request submitter to sign with account key
        raise Exception('not implemented!')

    path_base_str = '{chain_name}/{subdir}'.format(**locals())
    path_base = pathlib.Path(path_base_str)

    all_validators = []
    for inclusion_request in path_base.glob('genesis-inclusion-requests/*.toml'):
        print(":: adding {inclusion_request}".format(**locals()))
        request = toml.load(str(inclusion_request))

        # add validator node entries
        for validator in request['validators']:
            print(validator)
            all_validators.append(validator)

    if for_validator is None:
        config_filename = 'config.toml'
        connect_validators = all_validators
        p2p = default_ports['p2p']
        rpc = default_ports['rpc']
        app = default_ports['app']
        name = ''
    else:
        config_filename = for_validator + '-config.toml'
        connect_validators = [
            validator for validator in all_validators
            if validator['name'] != for_validator
        ]
        this_validator = next(validator for validator in all_validators
                if validator['name'] == for_validator)
        p2p = this_validator.get('p2p', default_ports['p2p'])
        rpc = this_validator.get('rpc', default_ports['rpc'])
        app = this_validator.get('app', default_ports['app'])
        name = this_validator['name']

    csv_validator_names = ', '.join([
        validator['name']
        for validator in connect_validators])
    csv_p2p_endpoints = ','.join([
        validator['host'] + ':' + str(validator.get('p2p', default_ports['p2p']))
        for validator in connect_validators])

    config = config_template.format(**locals())

    # write config file
    with (path_base / config_filename).open('w') as fh:
        fh.write(config)


if '__main__' == __name__:
    fire.Fire(main)
