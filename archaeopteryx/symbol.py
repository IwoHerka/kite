from .list import List


class Symbol(int):
    symbols = {}

    def __new__(cls, name, doc=None, canonical=None):
        s = cls.symbols.get(name)
        canonical = canonical or hash(name)

        if s is None:
            cls.symbols[name] = s = int.__new__(Symbol, canonical)

        s.name = name
        return s

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def eval(self, env, args=None):
        # Evaluation of a symbol is just
        # look-up of the value it refers to.
        return env.get(self.name)


T = Symbol('t')
F = List()
