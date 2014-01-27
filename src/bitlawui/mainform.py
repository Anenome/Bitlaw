#!/usr/bin/env python3
# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from .mylawtab import *
from .newlaw import *

class BitlawMainForm(QMainWindow):
    def newLaw(self):
        newLawWindow = NewLawEditor("", self)
        newLawWindow.show()

    def createAction(self, text, slot=None, shortcut=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if shortcut is not None:
            action.setShortcut(shortcut)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        action.setCheckable(checkable)
        return action
    
    def init_file_menu(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        newLawAction = self.createAction("&New...", self.newLaw, "Ctrl+N")
        self.fileMenu.addAction(newLawAction)
        fileQuitAction = self.createAction("&Quit", self.close, "Ctrl+Q")
        self.fileMenu.addAction(fileQuitAction)
    
    def init_editor(self):
        self.lawEditor = MyLawTab(self)
        self.tabs.addTab(self.lawEditor, "My laws")
        
    def init_adopted_laws(self):
        self.adoptedLaws = QWidget(self)
        self.tabs.addTab(self.adoptedLaws, "Adopted laws")
    
    def init_active_agreements(self):
        self.activeAgreements = QWidget(self)
        self.tabs.addTab(self.activeAgreements, "Active agreements")
    
    def init_expired_agreements(self):
        self.expiredAgreements = QWidget(self)
        self.tabs.addTab(self.expiredAgreements, "Expired agreements")
    
    def init_menus(self):
        self.init_file_menu()
    
    def init_tabs(self):
        self.tabs = QTabWidget(self)
        self.init_editor()
        self.init_adopted_laws()
        self.init_active_agreements()
        self.init_expired_agreements()
        self.setCentralWidget(self.tabs)
    
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setMinimumSize(640, 480)
        self.init_menus()
        self.init_tabs()