# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

import pickle
import time
import ..constants

Peer = namedtuple('Peer', ['host', 'port'])

def createDefaultNodes():
    knownNodes = {}

    # fill this out once I've found people who are willing to be default nodes 

    with open(PEERS_FILE, 'wb') as peerFile:
        pickle.dump(knownNodes, peerFile)
    return knownNodes

def readKnownNodes():
    knownNodes = {}
    with open(PEERS_FILE, 'rb') as peerFile:
        knownNodes = pickle.load(peerFile)
    return knownNodes