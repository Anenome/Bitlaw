#!/usr/bin/env python3
# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class LawEditor(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        rootLayout = QHBoxLayout(self)
        editorGroup = QGroupBox("Edit", self)
        viewerGroup = QGroupBox("View", self)
        rootLayout.addWidget(editorGroup)
        rootLayout.addWidget(viewerGroup)
        self.setLayout(rootLayout)