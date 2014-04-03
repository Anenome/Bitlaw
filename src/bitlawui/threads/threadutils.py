# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

import threading
from .constants import *
from ..config import *
from struct import pack, unpack

printLock = threading.Lock()
responseMessages = []
responseMessagesLock = threading.Lock()
shutdown = False

def isShutdownReady():
    return shutdown

def startShutdown():
    shutdown = True

def safePrint(*x):
    s = ""
    for obj in x:
        s += str(obj)
    with printLock:
        print(s)

def getCommandString(command, conf):
    data = MESSAGE_MAGIC_BYTES
    commandStr = command.append('\x00' * (8 - len(command)))
    data.append(commandStr)
    if command == 'ver':
        data.append(pack('>I', len(VERSION)))
        data.append(VERSION.encode())
    return data