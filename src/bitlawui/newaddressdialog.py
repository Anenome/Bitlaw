# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class NewAddressDialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)