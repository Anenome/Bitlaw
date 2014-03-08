# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from PyQt4.QtCore import *
from .protocol.key import *
from .utilities.constants import *

class Config:
    def loadKeys(self):
        try:
            with open(self.keyFileLocation, 'rb') as keyFile:
                # currently limited to 255 keys, may change later
                numKeys = keyFile.read(1)
                for i in range(numKeys):
                    k = Key()
                    k.loadFromFile(keyFile)
                    self.keys.append(k)
        except FileNotFoundError:
            pass

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
        self.settings.setValue("MainWindow/FirstTime", 'True')
        self.settings.setValue("Keys/FileLocation", KEYS_LOCATION)


    def __init__(self):
        self.keys = []