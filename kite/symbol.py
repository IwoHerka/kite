from .list import List


class Symbol(int):
    symbols = {}

    def __new__(cls, name, **kwargs):
        if not isinstance(name, str):
            raise TypeError(
                'Symbol name must be a string, got: {}'
                .format(name)
            )

        doc = kwargs.get('doc', None)
        canonical = kwargs.get('canonical', None)
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
        if args != None:
            raise TypeError(
                "Cannot apply '{}' to symbol '{}'"
                .format(args, self.name)
            )
        # Evaluation of a symbol is just
        # look-up of the value it refers to.
        return env.get(self.name)


class String(str):
    def __str__(self):
        return '"{}"'.format(super().__str__())

    def __repr__(self):
        return self.__str__()

    def eval(self, env, args=None):
        if args != None:
            raise TypeError(
                "Cannot apply '{}' to string '{}'"
                .format(args, str(self))
            )
        return self


T = Symbol('t')
F = List()
NIL = Symbol('NIL')
