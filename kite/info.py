VERSION = '0.0.1'

WELCOME_MSG = """\
Kite REPL, version: {}\
""".format(VERSION)

REPL_USAGE = """\
    ?, :h, :help    - Show help message
    :e, :env        - Show current dynamic environment
    :d, :del <name> - Delete name from the environment (todo)
    :b, :builtin    - Show built-in environment
    :l, :load       - Load source file\
"""

CMD_USAGE = """\
"""

PROMPT = '$'
DEPTH_MARK = '.'
HISTORY_FILE = '/home/siegmeyer/.lisphistory'

BUILTIN = ('atom', 'car', 'cdr', 'cons', 'eq',
           'cond', 'label', 'lambda', 'quote', 't', 'f', 'nil')

HELP = {
    'atom': 'help for atom',
    'car': 'dasdsad'
}
