# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from .mainform import *

def run():
    app = QApplication(sys.argv)
    app.setApplicationName("Bitlaw")
    form = BitlawMainForm()
    form.show()
    app.exec_()