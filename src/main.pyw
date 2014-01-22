#!/usr/bin/env python3
# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class BitlawMainForm(QMainWindow):
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
        fileQuitAction = self.createAction("&Quit", self.close, "Ctrl+Q")
        self.fileMenu.addAction(fileQuitAction)
    
    def init_menus(self):
        self.init_file_menu()
    
    def init_tabs(self):
        self.tabs = QTabWidget(self)
        # TODO: add tabs
        self.setCentralWidget(self.tabs)
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.init_menus()
        self.init_tabs()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Bitlaw")
    form = BitlawMainForm()
    form.show()
    app.exec_()