# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from ..pyelliptic.ecc import *
from ..threads.threadutils import *
from ..constants import *
from .key import *
import hashlib
from struct import *
import sys

def encodeInt(val, alphabet = ALPHABET):
    base = len(alphabet)
    result = ""
    while val > 0:
        rem = val % base
        result = str(alphabet[rem]) + result
        val = val // base
    return result

class Address:
    def __init__(self, hashValue, version=VERSION):
        self.version = version
        self.hashValue = hashValue
        self.encodedValue = ""

    def encodeVersion(self):
        # return the version as a big-endian unsigned byte.
        return pack('>B', self.version)

    def encode(self):
        a = self.encodeVersion() + self.hashValue
        sha = hashlib.new('sha512')
        sha.update(a)
        sha.update(sha.digest())
        checksum = sha.digest()[0:2]
        intValue = int.from_bytes(a + checksum, 'big')
        # this value is in base 64
        self.encodedValue = encodeInt(intValue)

def genKey():
    curve = ECC()
    pubKey = curve.get_pubkey()
    sha = hashlib.new('sha512')
    sha.update(pubKey)
    ripemd = hashlib.new('ripemd160')
    ripemd.update(sha.digest())
    sha.update(ripemd.digest())
    ripemd.update(sha.digest())
    #safePrint(ripemd.digest())
    a = Address(ripemd.digest())
    a.encode()
    key = Key(pubKey, curve.get_privkey(), a.encodedValue)
    return key