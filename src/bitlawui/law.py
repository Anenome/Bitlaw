#!/usr/bin/env python3
# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

class Law:
    def __init__(self, modified = False, filename = ""):
        self.modified = modified
        self.filename = filename
        self.hasFilename = not filename

    def writeToFile(self):
        pass

    def readFromFile(self):
        pass