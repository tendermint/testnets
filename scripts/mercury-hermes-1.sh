#! /bin/bash

# expects to be run from top of testnets repo

# set some environment variables 
export BCHOME_MERCURY_CLIENT=~/.cosmos-testnets/mercury/client
export BCHOME_MERCURY_SERVER=~/.cosmos-testnets/mercury/server
export TMHOME_MERCURY=~/.cosmos-testnets/mercury/server/tendermint
export BCHOME_HERMES_CLIENT=~/.cosmos-testnets/hermes/client
export BCHOME_HERMES_SERVER=~/.cosmos-testnets/hermes/server
export TMHOME_HERMES=~/.cosmos-testnets/hermes/server/tendermint

# make the directories
mkdir -p $TMHOME_HERMES $TMHOME_MERCURY

# create some aliases to use instead of raw `basecli` and `basecoin` to ensure we're using the right configuration for the chain we want to talk to.
alias basecli-mercury="basecli --home $BCHOME_MERCURY_CLIENT"
alias basecli-venus="basecli --home $BCHOME_HERMES_CLIENT"
alias basecoin-mercury="basecoin --home $BCHOME_MERCURY_SERVER"
alias basecoin-venus="basecoin --home $BCHOME_HERMES_SERVER"
alias tendermint-mercury="tendermint --home $TMHOME_MERCURY"
alias tendermint-hermes="tendermint --home $TMHOME_HERMES"

# copy the genesis and config files
cp mercury/tendermint/* $TMHOME_MERCURY
cp mercury/basecoin/* $BCHOME_MERCURY_SERVER
cp hermes/tendermint/* $TMHOME_HERMES
cp hermes/basecoin/* $BCHOME_HERMES_SERVER

