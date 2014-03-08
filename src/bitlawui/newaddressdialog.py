# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from .protocol.address import *

class NewAddressDialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setWindowTitle("New Address")
        textContent = "It appears that this is the first time you are running Bitlaw.\n" +\
            "You will need the following address to use the program.\n\n" +\
            "The address that has been generated for you is:\n"
        self.key = genKey()
        textContent += self.key.address
        text = QLabel(textContent, self)
        grid = QGridLayout()
        grid.addWidget(text, 0, 0, 2, 3)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        grid.addWidget(buttonBox, 2, 0, 1, 3)
        self.setLayout(grid)
        self.connect(buttonBox, SIGNAL("accepted()"), self, SLOT("accept()"))
