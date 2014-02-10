#!/usr/bin/env python3
# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from .common import *
from .law import *

class MyLawEditor(QWidget):
    nextId = 1

    def saveFileAs(self):
        index = self.tabs.currentIndex()
        if self.files[index].hasFilename():
            filename = self.files[index].getFilename()
        else:
            filename = ""
        filename = QFileDialog.getSaveFileName(self,
            "Bitlaw - Save Law", filename, "Law files (*.law)")
        if filename:
            if "." not in filename:
                filename += ".law"
            self.files[index].setFilename(filename)
            self.files[index].setModified(False)
            self.tabs.setTabText(index, filename)
            self.files[index].writeToFile()
            return True
        else:
            return False

    def saveFile(self):
        index = self.tabs.currentIndex()
        if not self.files[index].hasFilename():
            return self.saveFileAs()
        if not self.files[index].isModified():
            return False
        self.files[index].writeToFile()
        self.tabs.setTabText(index, self.tabs.tabText(index)[1:])
        self.files[index].setModified(False)
        return True

    def textChanged(self):
        index = self.tabs.currentIndex()
        if not self.files[index].isModified():
            self.files[index].setModified(True)
            self.tabs.setTabText(index, "*" + self.tabs.tabText(index))

    def addSection(self):
        index = self.tabs.currentIndex()
        widget = self.tabs.currentWidget()
        cursor = widget.textCursor()
        cursor.movePosition(QTextCursor.End)
        widget.setTextCursor(cursor)
        lineNo = str(widget.toPlainText()).count("\n")
        self.files[index].addSection(lineNo)
        self.editors[index].insertPlainText(self.files[index].getSection(-1).getName() + "\n")

    def addSubSection(self):
        pass

    def editorContextMenu(self, point):
        menu = QMenu()
        addMenu = menu.addMenu("Add")
        addMenu.addAction(createAction(self, "Add Section", self.addSection))
        addMenu.addAction(createAction(self, "Add Subsection", self.addSubSection))
        menu.exec_(self.editors[self.tabs.currentIndex()].mapToGlobal(point))

    def addFile(self, filename=""):
        if filename == "":
            filename = "Untitled-%d" % MyLawEditor.nextId
            MyLawEditor.nextId += 1
        editor = QTextEdit(self)
        editor.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(editor, SIGNAL("customContextMenuRequested(const QPoint&)"), self.editorContextMenu)
        self.connect(editor, SIGNAL("textChanged()"), self.textChanged)
        self.tabs.addTab(editor, filename)
        self.editors.append(editor)
        self.files.append(Law(False, filename))
        self.tabs.setCurrentIndex(len(self.files) - 1)

    def closeFile(self, index):
        pass

    def maybeSave(self, index):
        reply = QMessageBox.question(self, "File unsaved!",
            "Do you want to save " + self.files[index].getFilename() + " before closing it?",
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            if not self.saveFile():
                return False
            self.closeFile(index)
        elif reply == QMessageBox.No:
            self.closeFile(index)
        else:
            return False
        return True


    def tabClose(self, index):
        if not self.files[index].modified:
            self.tabs.removeTab(index)
            del self.files[index]
        else:
            if self.maybeSave(index):
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
        self.editors = []
        self.addFile()
