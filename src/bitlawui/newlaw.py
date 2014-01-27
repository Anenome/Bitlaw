#!/usr/bin/env python3
# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class NewLawEditor(QMainWindow):
    instances = set()
    nextId = 1

    def initFilename(self, filename):
        self.filename = filename
        if (self.filename == ""):
            self.filename = "Untitled-%d" % NewLawEditor.nextId
            NewLawEditor.nextId += 1
            self.editor.document().setModified(False)
        self.setWindowTitle(self.filename)

    def __init__(self, filename="", parent=None):
        QMainWindow.__init__(self, parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        NewLawEditor.instances.add(self)
        self.editor = QTextBrowser(self)
        self.setCentralWidget(self.editor)
        self.initFilename(filename)