# Testnets

This repository contains directories with the files required to join an identically named testnet.

See the links below for documentation on joining a public - or creating a local - testnet.

* [deploy tendermint testnets](http://tendermint.readthedocs.io/en/master/deploy-testnets.html)
* [join ethermint testnet](http://ethermint.readthedocs.io/en/develop/testnets/venus.html)
* [join/create gaia testnet](http://cosmos-sdk.readthedocs.io/en/develop/staking/intro.html)

## Config generation

1. install python3, (pip) install fire and toml libraries
1. run `python3 prepare-genesis-inclusion-requests.py <chain name>`
1. commit `<chain name>/gaia/genesis-inclusion-requests/request.toml.template`
1. collect pull requests as `<chain name>/gaia/genesis-inclusion-requests/<request>.toml` files
   * NB: such a request can add multiple validator nodes, and additional coins beside fermions
1. generate `genesis.json` and general purpose `config.toml` via
   * `python3 generate-genesis.py <chain name>`
   * `python3 generate-config.py <chain name>`
