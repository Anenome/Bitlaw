# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from threading import *
import socket
from ..constants import *
from .threadutils import *
from ..config import *
from struct import pack, unpack
import hashlib

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
    # bytes 16 through 19:  checksum of the payload
    # bytes 20 through (20 + payload length - 1):  data of the command
    def processData(self):
        if len(self.data) < 20:
            # can't read checksum correctly, exiting
            return
        if self.data[0:4] != MESSAGE_MAGIC_BYTES:
            safePrint("Message did not begin with the necessary byte signature.  Not looking at this message.")
            self.data = ''
            return
        command = self.data[4:12].decode().rstrip("\x00")
        payloadLength = unpack('>I', self.data[12:16])[0]
        safePrint("Payload is ", payloadLength, " bytes long.")
        payload = self.data[20: 20 + payloadLength]
        safePrint("Payload = ", payload)
        checksum = hashlib.sha512(payload).digest()[0:4]
        safePrint("checksum = ", checksum)
        if self.data[16:20] != checksum:
            safePrint("This message does not have the right checksum.  Exiting.")
            self.data = self.data[20 + payloadLength:]
            self.processData()
            return
        if command == 'ver':
            self.recVersion(payload)
        elif command == 'verack':
            self.recVerack()

    def recVersion(self, payload):
        payload = payload.decode()
        safePrint("Received version message.  Version =", payload)
        if (payload == VERSION):
            # do more complicated version matching later
            with responseMessagesLock:
                responseMessages.append(getCommandString('verack', self.config))

    def recVerack(self):
        safePrint("Received version acknowledgment.")