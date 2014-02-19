#!/usr/bin/env python3
# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from .law import *

class LawTextEdit(QTextEdit):
    # TODO: move code that finds the current line from MyLawEditor to this class
    def __init__(self, parent=None):
        QTextEdit.__init__(self, parent)
        self.linesEditable = [True]
        self.lineNo = 0
        self.connect(self, SIGNAL("cursorPositionChanged()"), self.cursorPositionChanged)

    def currentLineNumber(self):
        return self.lineNo

    def cursorPositionChanged(self):
        cursorPos = self.textCursor().position()
        text = self.toPlainText().splitlines()
        self.lineNo = 0
        l = 0
        for i in range(len(text)):
            l = len(text[i])
            if cursorPos > l:
                self.lineNo += 1
                cursorPos -= l
            else:
                break

    def keyPressEvent(self, event):
        # TODO: ensure non-editable lines cannot be modified
        # TODO: ensure non-editable lines cannot have newlines inserted in their middle
        acceptKey = True
        if event.key() == Qt.Key_Return:
            self.linesEditable.append(True)
        if acceptKey:
            QTextEdit.keyPressEvent(self, event)

    def setLineEditable(self, lineNumber, editable):
        self.linesEditable[lineNumber] = editable