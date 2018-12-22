from __future__ import print_function

import sys
from . import lisp


if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help'):
    print(lisp.USAGE)
else:
    print(lisp.WELCOME_MSG)
    lisp.repl()
