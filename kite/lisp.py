from __future__ import print_function

from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory

from .env import Environment
from .fn import (Function, add, atom, car, cdr, cond, cons, eq, label, lambda_,
                 quote)
from .info import *
from .list import List
from .parser import Parser
from .symbol import Symbol, T


def repl():
    """Start REPL."""
    env = get_environment()
    session = PromptSession()

    def startswith(instr, strings):
        for s in strings:
            if instr.startswith(s):
                return True

        return False

    while 1:
        instr = read_input(session.prompt)

        if instr in (':q', ':quit'):
            break
        elif startswith(instr, {'?', ':h', ':help'}):
            args = instr.strip().split(' ')

            if len(args) > 1:
                if args[1] in HELP:
                    print(HELP[args[1]])
                else:
                    print("No help available for '{}'".format(args[1]))
            else:
                print(REPL_USAGE)
        elif instr in (':e', ':env'):
            env.show(exclude=BUILTIN)
        elif instr in (':b', ':builtin'):
            env.show(include=BUILTIN)
        elif startswith(instr, {':l', ':load'}):
            args = instr.split(' ')

            if len(args) > 1:
                f = open(args[1], 'r')
                lines = f.read()
                parser = Parser()
                sexpr = parser.parse(lines)

                while sexpr:
                    try:
                        sexpr.eval(env)
                        print('Loaded: {}'.format(sexpr))
                        sexpr = parser.parse()
                    except Exception as e:
                        print(e)
                        break
            else:
                raise ValueError(':load requires an argument')
        else:
            sexpr = Parser().parse(instr)

            try:
                print(sexpr.eval(env))
            except Exception as e:
                print(e)


def read_input(prompt, line='', depth=0):
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
        return read_input(prompt, line, depth + 1)
    elif balance < 0:
        raise ValueError('Invalid parenthesis pattern')
    else:
        return line


def get_environment():
    return Environment({
        'quote':  Function(quote),
        'atom':   Function(atom),
        'car':    Function(car),
        'cdr':    Function(cdr),
        'cons':   Function(cons),
        'eq':     Function(eq),
        'label':  Function(label),
        'cond':   Function(cond),
        'lambda': Function(lambda_),
        '+':      Function(add),
        't':      Symbol('t'),
        'f':      Symbol('f'),
        'nil':    List()
    })
