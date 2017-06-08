# Announcing the Basecoin Testnets!

We're putting up two public testnets named `ball-n-chain` and `up-n-comer`,
both of which will run Basecoin on Tendermint with the Interblockchain Communication protocol,
so you can send tokens back and forth between them.

Here we describe how to run nodes, how to get coins, and how to use them from the command line.

# NOTICE

These are just testnets. Coins on these testnets have no monetary value. 
They do not in any way represent Atoms or any other digital currency. 
They are solely for testing.

# Install

Install [Basecoin](https://tendermint.com/download).

Fetch the repository of testnet data:

```
TESTNETS="$HOME/testnets"
git clone https://github.com/tendermint/testnets "$TESTNETS"
cd "$TESTNETS"
```

# Running Nodes

The `testnets` repository contains all the necessary `genesis.json` and `config.toml` files to sync with any of the testnets.

## Ball-N-Chain

To run a node on `ball-n-chain`, start Basecoin as follows:

```
BCHOME="$TESTNETS/ball-n-chain" basecoin start 
```

DNS names of validator nodes:
```
ball-n-chain-node0.testnets.interblock.io
ball-n-chain-node1.testnets.interblock.io
ball-n-chain-node2.testnets.interblock.io
ball-n-chain-node3.testnets.interblock.io
ball-n-chain-node4.testnets.interblock.io
ball-n-chain-node5.testnets.interblock.io
ball-n-chain-node6.testnets.interblock.io
```

If you want the server closest to you, you can choose from these aliases too:
```
ball-n-chain-ams2.testnets.interblock.io
ball-n-chain-fra1.testnets.interblock.io
ball-n-chain-lon1.testnets.interblock.io
ball-n-chain-nyc2.testnets.interblock.io
ball-n-chain-sfo2.testnets.interblock.io
ball-n-chain-sgp1.testnets.interblock.io
ball-n-chain-tor1.testnets.interblock.io
```

## Up-N-Comer

To run a node on `up-n-comer`, start Basecoin as follows:

```
BCHOME="$TESTNETS/up-n-comer" basecoin start 
```

DNS names of validator nodes:
```
up-n-comer-node0.testnets.interblock.io
up-n-comer-node1.testnets.interblock.io
up-n-comer-node2.testnets.interblock.io
up-n-comer-node3.testnets.interblock.io
up-n-comer-node4.testnets.interblock.io
up-n-comer-node5.testnets.interblock.io
up-n-comer-node6.testnets.interblock.io
```

If you want the server closest to you, you can choose from these aliases too:
```
up-n-comer-ams2.testnets.interblock.io
up-n-comer-fra1.testnets.interblock.io
up-n-comer-lon1.testnets.interblock.io
up-n-comer-nyc2.testnets.interblock.io
up-n-comer-sfo2.testnets.interblock.io
up-n-comer-sgp1.testnets.interblock.io
up-n-comer-tor1.testnets.interblock.io
```

# Get Some Coins

Generate a key for your account:

```
basecli keys new mykey
```

You'll need to enter and re-enter a passphrase. The command will then output an address.

Post your Cosmos address in the #testnet channel on the [Tendermint slack](), and wait for someone to send you some coins.

Once you have coins, you can send them around using the `basecli`. You'll need to know which chain you got the coins on.
For instance, if your coins are on `ball-n-chain`, you can send them to another account on `ball-n-chain` as follow:


Check the new balance:

```

```
