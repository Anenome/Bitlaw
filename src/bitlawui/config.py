# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from PyQt4.QtCore import *
from .protocol.key import *
from .utilities.constants import *
from struct import *

class Config:
    def loadKeys(self):
        try:
            with open(self.keyFileLocation, 'rb') as keyFile:
                # currently limited to 255 keys, may change later
                numKeys = unpack('>B', keyFile.read(1))[0]
                for i in range(numKeys):
                    k = Key()
                    k.loadFromFile(keyFile)
                    self.keys.append(k)
        except FileNotFoundError:
            pass

    def saveKeys(self):
        with open(self.keyFileLocation, 'wb') as keyFile:
            keyFile.write(pack(">B", len(self.keys)))
            for k in self.keys:
                k.writeToFile(keyFile)

    def loadFromQtSettings(self):
        self.settings = QSettings()
        self.geometry = self.settings.value("MainWindow/Geometry", None)
        if self.geometry is None:
            self.geometry = QRect(0,0,640,480)
        self.firstTime = self.settings.value("MainWindow/FirstTime", 'True')
        if self.firstTime == 'False':
            self.keyFileLocation = self.settings.value("Keys/FileLocation", "")
            if self.keyFileLocation != "":
                self.loadKeys()

    def saveToQtSettings(self):
        self.settings.setValue("MainWindow/Geometry", self.geometry)

        # just set this to true if testing is needed
        self.settings.setValue("MainWindow/FirstTime", 'False')
        self.settings.setValue("Keys/FileLocation", KEYS_LOCATION)
        self.saveKeys()


    def __init__(self):
        self.keys = []
        self.keyFileLocation = KEYS_LOCATION