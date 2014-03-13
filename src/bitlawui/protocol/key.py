# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from struct import *
import sys
from ..common import *

class Key:
    def __init__(self, pubKey = 0, privKey = 0, address = ""):
        self.pubEncryptionKey = pubKey
        self.privEncryptionKey = privKey
        self.address = address

    def loadFromFile(self, fileHandle):
        l = unpack('>B',fileHandle.read(1))[0]
        self.pubEncryptionKey = fileHandle.read(l)
        #print("pubEncryptionKey read:",self.pubEncryptionKey)
        l = unpack('>B',fileHandle.read(1))[0]
        self.privEncryptionKey = fileHandle.read(l)
        #print("privEncryptionKey read:",self.privEncryptionKey)
        l = unpack('>B',fileHandle.read(1))[0]
        self.address = fileHandle.read(l).decode()
        #print("address read:",self.address)
    def writeToFile(self, fileHandle):
        #print("pubEncryptionKey written:",self.pubEncryptionKey)
        fileHandle.write(pack('>B',len(self.pubEncryptionKey)))
        fileHandle.write(self.pubEncryptionKey)
        fileHandle.write(pack('>B',len(self.privEncryptionKey)))
        #print("privEncryptionKey written:",self.privEncryptionKey)
        fileHandle.write(self.privEncryptionKey)
        addrBytes = self.address.encode()
        #print("address written:",self.address)
        fileHandle.write(pack('>B',len(addrBytes)))
        fileHandle.write(addrBytes)