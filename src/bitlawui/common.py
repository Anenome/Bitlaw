# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

from PyQt4.QtCore import *
from PyQt4.QtGui import *

CODEC = "UTF-8"

LAW_TAG_NAME = "law"
LAW_SECTION_TAG_NAME = "section"
LAW_SECTION_TITLE_TAG_NAME = "title"
LAW_SECTION_TEXT_TAG_NAME = "text"

def createAction(parent, text, slot=None, shortcut=None, checkable=False, signal="triggered()"):
    action = QAction(text, parent)
    if shortcut is not None:
        action.setShortcut(shortcut)
    if slot is not None:
        parent.connect(action, SIGNAL(signal), slot)
    action.setCheckable(checkable)
    return action