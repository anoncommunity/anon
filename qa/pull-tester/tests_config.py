#!/bin/bash
# Copyright (c) 2013-2014 The Bitcoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

BUILDDIR="/Users/christopherarguello/Developer/anon2/anon"
EXEEXT=""

# These will turn into comments if they were disabled when configuring.
ENABLE_WALLET=1
ENABLE_UTILS=1
ENABLE_BITCOIND=1
ENABLE_ZMQ=1
#ENABLE_PROTON=1

REAL_BITCOIND="$BUILDDIR/src/anond${EXEEXT}"
REAL_BITCOINCLI="$BUILDDIR/src/anon-cli${EXEEXT}"
