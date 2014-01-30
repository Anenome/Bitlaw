#!/usr/bin/env python3
# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from .common import *
from .law import *

class MyLawEditor(QWidget):
    nextId = 1

    def addFile(self, filename=""):
        if (filename == ""):
            filename = "Untitled-%d" % MyLawEditor.nextId
            MyLawEditor.nextId += 1
        self.tabs.addTab(QWidget(self), filename)
        self.files.append(Law(False, filename))

    def tabClose(self, index):
        if not self.files[index].modified:
            self.tabs.removeTab(index)

    def __init__(self, filename="", parent=None):
        QWidget.__init__(self, parent)
        self.tabs = QTabWidget(self)
        self.tabs.setTabsClosable(True)
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        self.connect(self.tabs, SIGNAL("tabCloseRequested(int)"), self.tabClose)
        self.files = []
        self.addFile()