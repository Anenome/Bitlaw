#!/usr/bin/env python3
# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

class Law:
    def __init__(self, modified = False, filename = ""):
        self.modified = modified
        self.filename = filename
        self.hasFilenameValue = not filename
        self.sections = []

    def getSection(self, index):
        return self.sections[index]

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
        return len(self.sections)

    def writeToFile(self):
        pass

    def readFromFile(self):
        pass

    def addSection(self, lineNo):
        s = LawSection("Section " + str(self.getNumSections() + 1))
        s.setLineNumber(lineNo)
        print("Line number of new section is", s.getLineNumber())
        self.sections.append(LawSection("Section " + str(self.getNumSections() + 1)))

class LawSection:
    def __init__(self, name = ""):
        self.name = name
        self.subsections = []
        self.lineNum = 0
        self.text = ""
        # these are relative to lineNum
        # both are zero if there are no contents
        self.textStartLine = 0
        self.textEndLine = 0

    def getTextStartLine(self):
        return self.textStartLine

    def setTextStartLine(self, newVal):
        self.textStartLine = newVal

    def getTextEndLine(self):
        return self.textEndLine

    def setTextEndLine(self, newVal):
        self.textEndLine = newVal

    def setText(self, newText):
        self.text = newText
        self.textStartLine = 1
        self.textEndLine = newText.count("\n")

    def getText(self):
        return self.text

    def getLineNumber(self):
        return self.lineNum

    def setLineNumber(self, num):
        self.lineNum = num
        
    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getNumSubsections(self):
        return len(self.subsections)