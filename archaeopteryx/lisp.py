from __future__ import print_function

from prompt_toolkit import prompt

from .symbol import Symbol, T
from .env import Environment
from .symbol import Symbol
from .list import List
from .fn import quote, atom, car, cdr, cons, Function, eq, label

VERSION = '0.0.1'

WELCOME_MSG = """\
Archaeopteryx REPL, version: {}
""".format(VERSION)

USAGE = """\
usage: python -m archaeopteryx
"""

PROMPT = "$"
DEPTH_MARK = "."

def repl():
    """Start REPL."""

    while 1:
        user_input = get_command()
        print(user_input)


def get_command(line='', depth=0):
    line = line + ' ' if line else line

    if depth == 0:
        prompt_mark = PROMPT + ' '
    else:
        prompt_mark = PROMPT + ' ' + '{} '.format(DEPTH_MARK * (depth + 1))

    line = line + prompt(prompt_mark)

    balance = 0

    for ch in line:
        if ch == '(':
            balance += 1
        elif ch == ')':
            balance -= 1

    if balance > 0:
        return get_command(line, depth + 1)
    elif balance < 0:
        raise ValueError('Invalid parenthesis pattern')
    else:
        return line


def get_environment():
    env = Environment()

    env.set('quote', Function(quote))
    env.set('atom', Function(atom))
    env.set('car', Function(car))
    env.set('cdr', Function(cdr))
    env.set('cons', Function(cons))
    env.set('eq', Function(eq))
    env.set('label', Function(label))

    env.set('t', Symbol('t'))
    env.set('nil', List())
    env.set('f', List())

    return env


def eval(env, sexpr):
    return sexpr.eval(env)
