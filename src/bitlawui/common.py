# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from struct import *

def encodeVarInt(val):
    if val > (2 ** 64) - 1:
        return pack('>B', 16) + pack('>2Q', val)
    elif val > (2 ** 32) - 1:
        return pack('>B', 8) + pack('>Q', val)
    elif val > (2 ** 16) - 1:
        return pack('>B', 4) + pack('>I', val)
    elif val > (2 ** 8) - 1:
        return pack('>B', 2) + pack('>H', val)
    elif val > 0:
        return pack('>B', 1) + pack('>B', val)
    else:
        return b''

def decodeVarInt(val, l):
    if l > 8:
        res = unpack('>2Q', val)
    elif l > 4:
        res = unpack('>Q', val)
    elif l > 2:
        res = unpack('>I', val)
    elif l > 1:
        res = unpack('>H', val)
    else:
        res = unpack('>B', val)
    return res[0]

def createAction(parent, text, slot=None, shortcut=None, checkable=False, signal="triggered()"):
    action = QAction(text, parent)
    if shortcut is not None:
        action.setShortcut(shortcut)
    if slot is not None:
        parent.connect(action, SIGNAL(signal), slot)
    action.setCheckable(checkable)
    return action

if __name__ == '__main__':
    print("Enter an integer to encode:")
    toEncode = int(input())
    varIntEnc = encodeVarInt(toEncode)
    structEnc = pack('>Q', toEncode)
    print("Var int function:",varIntEnc)
    print("Struct function:",structEnc)
    print("Unpack result:", decodeVarInt(varIntEnc))