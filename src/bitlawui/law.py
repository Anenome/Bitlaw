#!/usr/bin/env python3
# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from .common import *
from PyQt4.QtXml import *

class Law:
    def __init__(self, modified = False, filename = ""):
        self.modified = modified
        self.filename = filename
        self.hasFilenameValue = filename != ""
        self.sections = []
        self.currentSection = None
        self.currentLineNo = 0

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

    def writeSection(self, stream, section):
        stream << "<section>\n"
        stream << "\t<title>\n"
        stream << "\t\t" + section.getName() + "\n"
        stream << "\t</title>\n"
        stream << "\t<text>\n"
        stream << "\t\t" + section.getText() + "\n"
        stream << "\t</text>\n"
        stream << "</section>\n"

    def writeToFile(self):
        fh = QFile(self.filenameValue)
        if not fh.open(QIODevice.WriteOnly):
            return
        stream = QTextStream(fh)
        stream.setCodec(CODEC)
        stream << "<?xml version='1.0' encoding='%s'?>\n" % CODEC
        stream << "<" + LAW_TAG_NAME + ">\n"
        for section in self.sections:
            self.writeSection(stream, section)
        stream << "</" + LAW_TAG_NAME + ">\n"
        if fh is not None:
            fh.close()

    def getText(self, node):
        child = node.firstChild()
        text = ""
        while not child.isNull():
            if child.nodeType() == QDomNode.TextNode:
                text += str(child.toText().data())
            child = child.nextSibling()
        return text.strip()

    def readSection(self, sectionElement):
        section = LawSection()
        name = text = None
        node = sectionElement.firstChild()
        while (name is None or text is None) and not node.isNull():
            if node.toElement().tagName() == LAW_SECTION_TITLE_TAG_NAME:
                section.setName(self.getText(node))
            elif node.toElement().tagName() == LAW_SECTION_TEXT_TAG_NAME:
                section.setText(self.getText(node))
            node = node.nextSibling()
        return section

    def readFromFile(self):
        # TODO: add proper error handling
        fh = QFile(self.filenameValue)
        dom = QDomDocument()
        if not fh.open(QIODevice.ReadOnly):
            return
        if not dom.setContent(fh):
            return
        if fh is not None:
            fh.close()
        root = dom.documentElement()
        if root.tagName() != LAW_TAG_NAME:
            return
        node = root.firstChild()
        while not node.isNull():
            if node.toElement().tagName() == LAW_SECTION_TAG_NAME:
                self.sections.append(self.readSection(node.toElement()))
            node = node.nextSibling()

    def searchSectionsByLineNo(self, lineNo, minIndex, maxIndex):
        if minIndex > maxIndex or len(self.sections) == 0:
            return None
        mid = int((maxIndex + minIndex) / 2)
        section = self.sections[mid]
        if section.getTextStartLine() > lineNo:
            return self.searchSectionsByLineNo(lineNo, minIndex, mid - 1)
        elif section.getTextEndLine() < lineNo:
            return self.searchSectionsByLineNo(lineNo, mid + 1, maxIndex)
        else:
            return section

    def setLineNumber(self, lineNo):
        self.currentLineNo = lineNo
        # the sections are guaranteed to be added in order of their lines, so it can be binary searched
        self.currentSection = self.searchSectionsByLineNo(lineNo, 0, len(self.sections) - 1)

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