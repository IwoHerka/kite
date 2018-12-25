import string

from .list import List
from .symbol import Symbol

SPECIAL = string.whitespace + '()'
# Occurance of special character
# delimits currently parsed token.


class Parser:
    def __init__(self):
        self.instr = None
        self.index = 0
        self.length = 0
        self.sexpr = []

    def current(self):
        return self.instr[self.index]

    def previous(self):
        return self.instr[self.index - 1]

    def parse(self, source=None):
        if source:
            self.instr = source
            self.length = len(self.instr)
            self.index = 0

        token = self.get_token()
        expr = None

        if token == ')':
            raise ValueError('Unexpected closing parenthesis')
        elif token == '(':
            return self.parse_([], self.get_token())

        elif token == "'":
            expr = []
            token = self.get_token()

            if token != '(':
                raise ValueError('Expected "(" after quote')
            else:
                token = self.get_token()

            expr = self.parse_([], token)

            return List(Symbol('quote'), List(*expr))
        else:
            return token

    def parse_(self, expr, token):
        while token != ')':
            if token in ("'", '('):
                self.index -= 1
                expr.append(self.parse())
            elif token == None:
                raise ValueError("Invalid end of expression: ", self.instr)
            else:
                expr.append(token)

            token = self.get_token()

        return List(*expr)

    def get_token(self):
        if self.index >= self.length:
            return None

        while self.index < self.length and self.current() in string.whitespace:
            self.index += 1

        if self.index == self.length:
            return None

        elif self.current() in "'()":
            self.index += 1
            return self.previous()

        elif self.current() == '"':
            tokenstr = ''
            self.index += 1

            while self.current() != '"' and self.index < self.length:
                tokenstr += self.current()
                self.index += 1

            self.index += 1
            return String(tokenstr)

        else:
            token_str = ''

            while self.index < self.length:
                if self.current() in SPECIAL:
                    break
                else:
                    token_str += self.current()
                    self.index += 1

            return Symbol(token_str)
