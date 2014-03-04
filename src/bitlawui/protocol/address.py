# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from ..pyelliptic.ecc import *
from ..utilities.threadutils import *
import hashlib

def genAddress():
    curve = ECC()
    pub_key = curve.get_pubkey()
    sha = hashlib.new('sha512')
    sha.update(pub_key)
    ripemd = hashlib.new('ripemd160')
    ripemd.update(sha.digest())
    safePrint(ripemd.digest())
    return None