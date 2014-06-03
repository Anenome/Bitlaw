# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

import pickle
import time
from collections import *
from ..config import *
import threading

Peer = namedtuple('Peer', ['host', 'port'])
knownPeers = {}
knownPeersLock = threading.Lock() 
connectedPeers = {}

def createDefaultNodes(fileName):
    # fill this out once I've found people who are willing to be default nodes 

    writeKnownNodes(fileName)
        

def writeKnownNodes(fileName):
    with open(fileName, 'wb') as peerFile:
        pickle.dump(knownPeers, peerFile)

def readKnownNodes(fileName):
    global knownPeers
    try:
        with open(fileName, 'rb') as peerFile:
            knownPeers = pickle.load(peerFile)
        # remove nodes that are more than 48 hours old

    except FileNotFoundError:
        pass

def addKnownPeer(peer, timestamp):
    knownPeers[peer] = timestamp

def addConnectedPeer(peer, timestamp):
    connectedPeers[peer] = timestamp