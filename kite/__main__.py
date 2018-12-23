from __future__ import print_function

import sys
from .info import CMD_USAGE, WELCOME_MSG
from .lisp import repl


if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help'):
    print(CMD_USAGE)
else:
    print(WELCOME_MSG)
    repl()
