# Announcing the Basecoin Testnets!

We're putting up two public testnets named `mercury` and `hermes`,
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

To run a node on `mercury`, start Basecoin as follows:

```
BCHOME="$TESTNETS/mercury" basecoin start 
```

DNS names of validator nodes:
```
mercury-node0.testnets.interblock.io
mercury-node1.testnets.interblock.io
mercury-node2.testnets.interblock.io
mercury-node3.testnets.interblock.io
mercury-node4.testnets.interblock.io
mercury-node5.testnets.interblock.io
mercury-node6.testnets.interblock.io
```

If you want the server closest to you, you can choose from these aliases too:
```
mercury-ams2.testnets.interblock.io
mercury-fra1.testnets.interblock.io
mercury-lon1.testnets.interblock.io
mercury-nyc3.testnets.interblock.io
mercury-sfo2.testnets.interblock.io
mercury-sgp1.testnets.interblock.io
mercury-tor1.testnets.interblock.io
```

## Up-N-Comer

To run a node on `hermes`, start Basecoin as follows:

```
BCHOME="$TESTNETS/hermes" basecoin start 
```

DNS names of validator nodes:
```
hermes-node0.testnets.interblock.io
hermes-node1.testnets.interblock.io
hermes-node2.testnets.interblock.io
hermes-node3.testnets.interblock.io
hermes-node4.testnets.interblock.io
hermes-node5.testnets.interblock.io
hermes-node6.testnets.interblock.io
```

If you want the server closest to you, you can choose from these aliases too:
```
hermes-ams2.testnets.interblock.io
hermes-fra1.testnets.interblock.io
hermes-lon1.testnets.interblock.io
hermes-nyc3.testnets.interblock.io
hermes-sfo2.testnets.interblock.io
hermes-sgp1.testnets.interblock.io
hermes-tor1.testnets.interblock.io
```

# Get Some Coins

Generate a key for your account:

```
basecli keys new mykey
```

You'll need to enter and re-enter a passphrase. The command will then output an address.

Post your Cosmos address in the #testnet channel on the [Tendermint slack](), and wait for someone to send you some coins.

Once you have coins, you can send them around using the `basecli`. You'll need to know which chain you got the coins on.
For instance, if your coins are on `mercury`, you can send them to another account on `mercury` as follow:


Check the new balance:

```

```
