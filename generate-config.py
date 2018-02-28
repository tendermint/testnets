#!/usr/bin/env python3

import datetime
import json
import pathlib

import fire
import toml


config_template = """# https://github.com/toml-lang/toml

proxy_app = "tcp://127.0.0.1:{app}"
moniker = "{moniker}"
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
# sentry names: {csv_sentry_names}
seeds = "{csv_p2p_endpoints}"
"""

default_ports = {
    'p2p': 46656,
    'rpc': 46657,
    'app': 46658,
}
default_moniker = ""


def main(chain_name, subdir='gaia', skip_sig_checks=True):
    """Specify validator "name" from one of the genesis inclusion requests
    to create a customized config file."""

    if not skip_sig_checks:
        # idea is for request submitter to sign with account key
        raise Exception('not implemented!')

    path_base_str = '{chain_name}/{subdir}'.format(**locals())
    path_base = pathlib.Path(path_base_str)

    all_validators = []
    all_sentries = []
    for inclusion_request in path_base.glob('genesis-inclusion-requests/*.toml'):
        print(":: adding {inclusion_request}".format(**locals()))
        request = toml.load(str(inclusion_request))

        # add validator node entries
        for validator in request['validator']:
            print(validator)
            all_validators.append(validator)

        for sentry in request['sentry']:
            print(sentry)
            all_sentries.append(sentry)

    config_filename = 'config.toml'

    csv_sentry_names = ', '.join([
        sentry.get('name', '')
        for sentry in all_sentries])
    csv_p2p_endpoints = ','.join([
        sentry['host'] + ':' + str(sentry.get('p2p', default_ports['p2p']))
        for sentry in all_sentries])

    p2p = default_ports['p2p']
    rpc = default_ports['rpc']
    app = default_ports['app']
    moniker = default_moniker

    config = config_template.format(**locals())

    # write config file
    with (path_base / config_filename).open('w') as fh:
        fh.write(config)


if '__main__' == __name__:
    fire.Fire(main)
