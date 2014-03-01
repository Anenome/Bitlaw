# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from .common import *
from .mylaweditor import *
from .pyelliptic import *
from .newaddressdialog import *

class BitlawMainForm(QMainWindow):
    def loadSettings(self):
        self.settings = QSettings()
        geo = self.settings.value("MainWindow/Geometry", None)
        if geo is not None:
            self.restoreGeometry(self.settings.value("MainWindow/Geometry"))    
        else:
            self.setGeometry(0, 0, 640, 480)
        self.firstTime = self.settings.value("MainWindow/FirstRun", True)

    def maybeSave(self):
        for index in range(len(self.newLaws.files)):
            if self.newLaws.files[index].modified:
                if not self.newLaws.maybeSave(index):
                    return False
        return True

    def saveSettings(self):
        self.settings.setValue("MainWindow/Geometry", self.saveGeometry())
        self.settings.setValue("MainWindow/FirstRun", False)

    def closeEvent(self, event):
        if self.maybeSave():
            self.saveSettings()
            event.accept()
        else:
            event.ignore()

    def tabChanged(self, index):
        if index == 0:
            self.saveLawAction.setEnabled(True)
            self.saveLawAsAction.setEnabled(True)
        else:
            self.saveLawAction.setEnabled(False)
            self.saveLawAsAction.setEnabled(False)

    def newLaw(self):
        self.tabs.setCurrentIndex(0)
        self.tabs.widget(0).addFile()

    def saveLaw(self):
        if self.tabs.currentIndex() == 0:
            self.newLaws.saveFile()

    def saveLawAs(self):
        if self.tabs.currentIndex() == 0:
            self.newLaws.saveFileAs()

    def openLaw(self):
        if self.tabs.currentIndex() == 0:
            self.newLaws.openFile()

    def initFileMenu(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.newLawAction = createAction(self, "&New...", self.newLaw, "Ctrl+N")
        self.fileMenu.addAction(self.newLawAction)
        self.openLawAction = createAction(self, "&Open...", self.openLaw, "Ctrl+O")
        self.fileMenu.addAction(self.openLawAction)
        self.saveLawAction = createAction(self, "&Save", self.saveLaw, "Ctrl+S")
        self.fileMenu.addAction(self.saveLawAction)
        self.saveLawAsAction = createAction(self, "Save As...", self.saveLawAs, "Ctrl+Shift+S")
        self.fileMenu.addAction(self.saveLawAsAction)
        fileQuitAction = createAction(self, "&Quit", self.close, "Ctrl+Q")
        self.fileMenu.addAction(fileQuitAction)

    def initNewLaws(self):
        self.newLaws = MyLawEditor(self)
        self.tabs.addTab(self.newLaws, "Edit laws")
    
    def initMyLaws(self):
        self.myLaws = QWidget(self)
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
        self.initNewLaws()
        self.initMyLaws()
        self.initAdoptedLaws()
        self.initActiveAgreements()
        self.initExpiredAgreements()
        self.setCentralWidget(self.tabs)

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.loadSettings()
        self.initMenus()
        self.initTabs()
        self.show()
        if self.firstTime:
            newAddressDialog = NewAddressDialog(self)
            if newAddressDialog.exec_():
                # do stuff here
                pass