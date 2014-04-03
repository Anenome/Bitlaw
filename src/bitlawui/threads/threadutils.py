# Copyright (c) 2014 Johan Burke
# Distributed under the MIT software license.  See http://www.opensource.org/licenses/mit-license.php.

import threading

# global variables are bad!
# don't refer to this directly, use safePrint(x)
printLock = threading.Lock()

def safePrint(x):
    with printLock:
        print(x)