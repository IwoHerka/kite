class List:
    def __init__(self, *args):
        self.data = tuple(args) or tuple()

    def car(self):
        return self.data[0]

    def cdr(self):
        return List(*self.data[1:])

    def cons(self, other):
        return List([e] + other)

    def eval(self, env, args=None):
        return self.car().eval(env).eval(env, self.cdr())

    def __eq__(self, other):
        if isinstance(other, List):
            return self.data == other.data

        return False
