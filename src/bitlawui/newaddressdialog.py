# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class NewAddressDialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setWindowTitle("New Address")
        textContent = "It appears that this is the first time you are running Bitlaw.\n" +\
            "An address will be created for you automatically."
        text = QLabel(textContent, self)
        grid = QGridLayout()
        grid.addWidget(text, 0, 0, 2, 3)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        grid.addWidget(buttonBox, 2, 0, 1, 3)
        self.setLayout(grid)
        self.connect(buttonBox, SIGNAL("accepted()"), self, SLOT("accept()"))
        self.connect(buttonBox, SIGNAL("rejected()"), self, SLOT("reject()"))