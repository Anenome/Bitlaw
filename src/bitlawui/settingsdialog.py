# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from .protocol.address import *
from .config import *
from .common import *

class AddressSettings(QWidget):
    def populateList(self):
        self.addressesList.clear()
        for key in self.config.keys:
            item = QListWidgetItem(key.address)
            self.addressesList.addItem(item)

    def copyAddress(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.addressesList.currentItem().text())

    def addressesContextMenu(self, point):
        menu = QMenu()
        menu.addAction(createAction(self, "Copy", self.copyAddress))
        menu.exec_(self.addressesList.mapToGlobal(point))

    def __init__(self, parent, config):
        QWidget.__init__(self, parent)

        self.config = config

        layout = QGridLayout(self)

        self.addressesList = QListWidget()
        self.populateList()
        self.addressesList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self.addressesList, SIGNAL("customContextMenuRequested(const QPoint&)"), self.addressesContextMenu)

        layout.addWidget(self.addressesList, 1, 1)

        self.setLayout(layout)

class SettingsDialog(QDialog):
    def __init__(self, parent, config):
        QDialog.__init__(self, parent)
        self.setWindowTitle("Settings")
        layout = QGridLayout(self)
        self.addresses = AddressSettings(self, config)
        self.tabs = QTabWidget(self)
        self.tabs.addTab(self.addresses, "Addresses")
        layout.addWidget(self.tabs, 1, 1)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.connect(buttonBox, SIGNAL("accepted()"), self.accept)
        self.connect(buttonBox, SIGNAL("rejected()"), self.reject)
        layout.addWidget(buttonBox, 2, 1)
        self.setLayout(layout)