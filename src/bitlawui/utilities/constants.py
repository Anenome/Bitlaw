# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

# This file includes constants used by several files.  DO NOT CHANGE THEIR VALUES.
import os.path

CODEC = "UTF-8"

LAW_TAG_NAME = "law"
LAW_SECTION_TAG_NAME = "section"
LAW_SECTION_TITLE_TAG_NAME = "title"
LAW_SECTION_TEXT_TAG_NAME = "text"

VERSION = 1
ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+-"
KEYS_LOCATION = os.path.expanduser("~/Bitlaw/keys.dat")