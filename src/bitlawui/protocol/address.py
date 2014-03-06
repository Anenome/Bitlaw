# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from ..pyelliptic.ecc import *
from ..utilities.threadutils import *
from ..utilities.constants import *
import hashlib
from struct import *

class Address:
    def __init__(self, hashValue, version=VERSION):
        self.version = version
        self.hashValue = hashValue

    def encodeVersion(self):
        return pack('>B', self.version)

    def encode(self):
        a = self.encodeVersion() + self.hashValue
        safePrint(a)
        sha = hashlib.new('sha512')
        sha.update(a)
        sha.update(sha.digest())
        checksum = sha.digest()[0:4]

def genAddress():
    curve = ECC()
    pub_key = curve.get_pubkey()
    sha = hashlib.new('sha512')
    sha.update(pub_key)
    ripemd = hashlib.new('ripemd160')
    ripemd.update(sha.digest())
    sha.update(ripemd.digest())
    ripemd.update(sha.digest())
    #safePrint(ripemd.digest())
    a = Address(ripemd.digest())
    a.encode()
    return a