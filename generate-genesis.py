#!/usr/bin/env python3

import datetime
import json
import pathlib

import fire
import toml


def main(chain_name, subdir='gaia', skip_sig_checks=True):
    if not skip_sig_checks:
        # idea is for request submitter to sign with account key
        raise Exception('not implemented!')

    genesis = dict()
    genesis['genesis_time'] = datetime.datetime.utcnow().isoformat()
    genesis['chain_id'] = chain_name

    genesis['validators'] = list()

    genesis['app_options'] = dict()
    genesis['app_options']['accounts'] = list()

    # two unclear items
    genesis['app_hash'] = ''
    genesis['app_options']['plugin_options'] = [
        "coin/issuer", {"app": "sigs", "addr": "B01C264BFE9CBD45458256E613A6F07061A3A6B6"}
    ]

    path_base_str = '{chain_name}/{subdir}'.format(**locals())
    path_base = pathlib.Path(path_base_str)

    for inclusion_request in path_base.glob('genesis-inclusion-requests/*.toml'):
        print(":: adding {inclusion_request}".format(**locals()))
        request = toml.load(str(inclusion_request))

        # add validator node entries
        for validator in request['validator']:
            print(validator)
            validator_entry = {
                "name": validator['name'],
                "pub_key": {
                    "data": validator['pub_key'],
                    "type": "ed25519",
                },
                "power": validator['power'],
            }
            genesis['validators'].append(validator_entry)

        # add account with coins
        account = request['account']
        account_entry = {
            "name": account['name'],
            "address": account['address'],
            "coins": [],
        }

        for coin_name, coin_amount in request['coins'].items():
            coin_entry = {
                "denom": coin_name,
                "amount": coin_amount,
            }
            account_entry['coins'].append(coin_entry)
        genesis['app_options']['accounts'].append(account_entry)

    # write genesis.json
    with (path_base / 'genesis.json').open('w') as fh:
        fh.write(json.dumps(genesis, indent=2))


if '__main__' == __name__:
    fire.Fire(main)
