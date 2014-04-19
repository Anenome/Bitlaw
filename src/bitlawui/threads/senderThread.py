# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from threading import *
import socket
from ..constants import *
from .threadutils import *
from ..config import *
from struct import pack, unpack

class SenderThread(Thread):
    def __init__(self, config):
        Thread.__init__(self)
        self.config = config

    def setup(self, sock):
        self.sock = sock
        self.data = b''

    def sendVerMsg(self):
        msg = getCommandString('ver', self.config)
        safePrint("Message to be sent is: ", msg)
        try:
            self.sock.sendall(msg)
        except Exception as err:
            safePrint("Error while sending version message:", err)

    def run(self):
        while True:
            if isShutdownReady():
                safePrint("Shutting down sender thread.")
                try:
                    safePrint("Closing connection in sender thread.")
                    self.sock.shutdown(socket.SHUT_RDWR)
                    self.sock.close()
                except Exception as err:
                    safePrint("Error while closing connection: ", err)
                break
            else:
                msg = ''
                with responseMessagesLock:
                    if len(responseMessages) != 0:
                        msg = responseMessages.pop(0)
                        safePrint('msg = ', msg)
                if msg != '':
                    self.sock.sendall(msg)