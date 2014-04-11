# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from threading import *
import socket
from ..constants import *
from .threadutils import *
from ..config import *
from struct import pack, unpack

class ReceiverThread(Thread):
    def __init__(self, config):
        Thread.__init__(self)
        self.config = config
        

    def setup(self, sock):
        self.sock = sock
        self.data = b''

    def run(self):
        while True:
            if isShutdownReady():
                safePrint("Shutdown signal received.  Stopping receiver thread.")
                break
            dataLength = len(self.data)
            try:
                safePrint("Attempting to receive data.")
                self.data += self.sock.recv(4096)
            except socket.timeout:
                safePrint("Socket timed out in receiver thread.")
                break
            except Exception as err:
                break

            # close the connection if no new data was received
            if len(self.data) == dataLength:
                safePrint("Received no data.  Breaking.")
                break
            else:
                self.processData()
    # a message is structured in the following way:
    # bytes 0 through 3:  byte signature common to all messages.
    # bytes 4 through 11:  the command, padded at the end if necessary
    # bytes 12 through 15:  the payload length
    # bytes 16 through (16 + payload length - 1):  data of the command
    def processData(self):
        if self.data[0:4] != MESSAGE_MAGIC_BYTES:
            safePrint("Message did not begin with the necessary byte signature.  Not looking at this message.")
            self.data = ''
            return
        command = self.data[4:12].decode()
        payloadLength = unpack('>I', self.data[12:16])[0]
        if command == 'ver\x00\x00\x00\x00\x00':
            self.recVersion(self.data[16:16+payloadLength])
    def recVersion(self, payload):
        safePrint("Received version message.  Version =", payload)