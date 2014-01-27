#!/usr/bin/env python3
# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from .mylawtab import *
from .newlaw import *

class BitlawMainForm(QMainWindow):
    def newLaw(self):
        NewLawEditor().show()

    def createAction(self, text, slot=None, shortcut=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if shortcut is not None:
            action.setShortcut(shortcut)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        action.setCheckable(checkable)
        return action
    
    def initFileMenu(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        newLawAction = self.createAction("&New...", self.newLaw, "Ctrl+N")
        self.fileMenu.addAction(newLawAction)
        fileQuitAction = self.createAction("&Quit", self.close, "Ctrl+Q")
        self.fileMenu.addAction(fileQuitAction)
    
    def initMyLaws(self):
        self.myLaws = MyLawTab(self)
        self.tabs.addTab(self.myLaws, "My laws")
        
    def initAdoptedLaws(self):
        self.adoptedLaws = QWidget(self)
        self.tabs.addTab(self.adoptedLaws, "Adopted laws")
    
    def initActiveAgreements(self):
        self.activeAgreements = QWidget(self)
        self.tabs.addTab(self.activeAgreements, "Active agreements")
    
    def initExpiredAgreements(self):
        self.expiredAgreements = QWidget(self)
        self.tabs.addTab(self.expiredAgreements, "Expired agreements")
    
    def initMenus(self):
        self.initFileMenu()
    
    def initTabs(self):
        self.tabs = QTabWidget(self)
        self.initMyLaws()
        self.initAdoptedLaws()
        self.initActiveAgreements()
        self.initExpiredAgreements()
        self.setCentralWidget(self.tabs)
    
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setMinimumSize(640, 480)
        self.initMenus()
        self.initTabs()