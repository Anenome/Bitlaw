#!/usr/bin/env python3
# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from .law import *

class LawTextEdit(QTextEdit):
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

    def isPrinting(self, key):
        return key >= Qt.Key_Space and key <= Qt.Key_ydiaeresis

    def keyPressEvent(self, event):
        # TODO: ensure non-editable lines cannot be modified
        # TODO: ensure non-editable lines cannot have newlines inserted in their middle
        print("Editable lines:",self.linesEditable)
        acceptKey = self.linesEditable[self.lineNo]
        checkLines = False
        l = 0
        if not self.isPrinting(event.key()):
            QTextEdit.keyPressEvent(self, event)
        elif acceptKey:
            if event.key() == Qt.Key_Return:
                self.linesEditable.append(True)
            elif event.key() == Qt.Key_Backspace:
                checkLines = True
                l = self.lineNo
            QTextEdit.keyPressEvent(self, event)
            #TODO: fix this
            if checkLines:
                if str(self.toPlainText()).count('\n') < len(self.linesEditable):
                    del self.linesEditable[l]

    def setLineEditable(self, lineNumber, editable):
        self.linesEditable[lineNumber] = editable

    def insertPlainText(self, text):
        QTextEdit.insertPlainText(self, text)
        for i in range(text.count('\n')):
            self.linesEditable.insert(self.lineNo + i, True)