# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from struct import *

class Key:
    def __init__(self, pubKey = 0, privKey = 0, address = ""):
        self.pubEncryptionKey = 0
        self.privEncryptionKey = 0
        self.address = address

    def loadFromFile(self, fileHandle):
        numBytes = fileHandle.read(4)
        self.pubEncryptionKey = fileHandle.read(numBytes)
        numBytes = fileHandle.read(4)
        self.privEncryptionKey = fileHandle.read(numBytes)
        numBytes = fileHandle.read(4)
        self.address = fileHandle.read(numBytes)
    def writeToFile(self, fileHandle):
        fileHandle.write(pack(">I", len(self.pubEncryptionKey)))
        fileHandle.write(self.pubEncryptionKey)
        fileHandle.write(pack(">I", len(self.privEncryptionKey)))
        fileHandle.write(self.privEncryptionKey)
        fileHandle.write(pack(">I", len(self.address)))
        fileHandle.write(self.address)