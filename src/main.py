#!/usr/bin/env python3
# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
        
class Main:
    def start(self):
        # perform other initialization stuff here too
        import bitlawui
        bitlawui.run()

if __name__ == "__main__":
    main = Main()
    main.start()