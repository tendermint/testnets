## Overview

These scripts are intended to support the following workflow:

* Initiator generates a "genesis inclusion request" template file by running
`python3 scripts/chainsetup/prepare-genesis-inclusion-requests.py <chain_id>`
  from the root directory. The resulting file `<chain_id>/gaia/genesis-inclusion-requests/request.toml.template`
  is committed and advertised ed to interested parties.
* Each test validator forks the repo, generates a file `<validator_name>.toml` in the same directory,
  commits and sends a pull request
* The initiator approves all pull requests, and runs
`python3 scripts/chainsetup/generate-config.py <chain_id>` and
`python3 scripts/chainsetup/generate-genesis.py <chain_id>`. The resulting files are committed and published,
   possibly using a signed git tag. They are:
```
   <chain_id>/gaia/genesis.json
   <chain_id>/gaia/config.toml
```
* The validators deploy their nodes using `genesis.json` as-is, and `config.toml` with necessary changes.

The result of this is:
* all validator requests are auditable
* everything is asynchronous
* the genesis file is created in a deterministic, verifiable way (apart from the timestamp...)

## Prerequisites

Python >=3.6, with the fire and toml libraries.

Via pip: `pip install -r requirements.txt`

Using [conda](https://conda.io/docs/user-guide/install/index.html): `conda env update -f environment.yaml`

## Flexibility

In the typical case, a validator simply fills out the blanks in the template.

Alternative use cases are:
* multiple `[[validator]]` sections (to support multiple pubkeys)
* multiple `[[sentry]]` sections (to support multiple P2P seed endpoints)
* multiple `[coin]` entries besides fermions
