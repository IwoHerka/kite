class List:
    def __init__(self, *args):
        self.data = tuple(args) or tuple()

    def car(self):
        return self.data[0]

    def cdr(self):
        return List(*self.data[1:])

    def cons(self, other):
        return List(*([other] + list(self.data)))

    def eval(self, env, args=None):
        if self.data:
            return self.car().eval(env).eval(env, self.cdr())
        else:
            # Empty list evalautes to itself.
            return self

    def __eq__(self, other):
        if isinstance(other, List):
            return self.data == other.data

        return False

    def __repr__(self):
        return '({})'.format(' '.join(str(d) for d in self.data))

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)
