#!/usr/bin/env python3
# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

class Law:
    def __init__(self, modified = False, filename = ""):
        self.modified = modified
        self.filename = filename
        self.hasFilenameValue = not filename
        self.numSections = 0

    def isModified(self):
        return self.modified

    def setModified(self, modified):
        self.modified = modified

    def getFilename(self):
        return self.filename

    def setFilename(self, filename):
        if filename:
            self.hasFilename = True
            self.filenameValue = filename

    def hasFilename(self):
        return self.hasFilenameValue

    def getNumSections(self):
        return self.numSections

    def writeToFile(self):
        pass

    def readFromFile(self):
        pass

    def addSection(self):
        self.numSections += 1

class LawSection:
    def __init__(self, name = ""):
        self.name = name

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName