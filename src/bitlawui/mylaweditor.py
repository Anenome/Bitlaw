#!/usr/bin/env python3
# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from .common import *
from .law import *

class MyLawEditor(QWidget):
    nextId = 1

    def saveFile(self):
        index = self.tabs.currentIndex()
        self.files[index].writeToFile()
        self.tabs[index].setTabText(self.tabs[index].tabText(index)[1:])
        self.files[index].modified = False

    def textChanged(self):
        index = self.tabs.currentIndex()
        if not self.files[index].modified:
            self.files[index].modified = True
            self.tabs.setTabText(index, "*" + self.tabs.tabText(index))

    def addFile(self, filename=""):
        if filename == "":
            filename = "Untitled-%d" % MyLawEditor.nextId
            MyLawEditor.nextId += 1
        editor = QTextEdit(self)
        self.connect(editor, SIGNAL("textChanged()"), self.textChanged)
        self.tabs.addTab(editor, filename)
        self.files.append(Law(False, filename))
        self.tabs.setCurrentIndex(len(self.files) - 1)

    def closeFile(self, index):
        pass

    def tabClose(self, index):
        if not self.files[index].modified:
            self.tabs.removeTab(index)
            del self.files[index]
        else:
            reply = QMessageBox.question(self, "File unsaved!",
                "Do you want to save " + self.files[index].filename + " before closing it?",
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if reply == QMessageBox.Yes:
                self.files[index].writeToFile()
                self.closeFile(index)
                self.tabs.removeTab(index)
                del self.files[index]
            elif reply == QMessageBox.No:
                self.closeFile(index)
                self.tabs.removeTab(index)
                del self.files[index]

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
