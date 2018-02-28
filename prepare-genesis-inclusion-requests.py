#!/usr/bin/env python3

import pathlib

# import ed25519
import fire


basic_template = """[chain]
name = "{chain_name}"

[account]
name = ""
address = ""

[coins]
fermion = {balance}

[[sentry]]
host = ""
p2p = {p2p}

[[validator]]
name = ""
pub_key = ""
power = {power}
"""


def main(chain_name, subdir='gaia', power=1000, p2p=46656, rpc=46657, balance=10000):
    # path_str = f'{chain_name}/{subdir}/genesis-inclusion-requests'
    path_str = '{chain_name}/{subdir}/genesis-inclusion-requests'.format(**locals())
    path = pathlib.Path(path_str)
    path.mkdir(parents=True, exist_ok=True)

    # chain_pub_key = ed25519.create_keypair()[1].to_ascii(encoding='hex').decode().upper()
    content = basic_template.format(**locals())
    with (path / 'request.toml.template').open('w') as fh:
        fh.write(content)

if '__main__' == __name__:
    fire.Fire(main)
