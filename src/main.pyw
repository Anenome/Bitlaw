#!/usr/bin/env python
# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class BitlawMainForm(QMainWindow):
    def init_file_menu(self):
        self.fileMenu = self.menuBar().addMenu("&File")
    
    def init_menus(self):
        self.init_file_menu()
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.init_menus()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Bitlaw")
    form = BitlawMainForm()
    form.show()
    app.exec_()