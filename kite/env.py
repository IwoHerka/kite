class Environment:
    def __init__(self, bindings=None):
        self.stack = [bindings or {}]
        self.index = 0

    def set(self, name, val, i=None):
        """
        Assign value to a name. By default, names will be
        stored in the lowest scope possible.
        """
        i = i if i != None else self.index

        if name in self.stack[i]:
            self.stack[i][name] = val
        elif i > 0:
            self.set(name, val, i - 1)
        else:
            self.stack[i][name] = val

    def get(self, name, i=None):
        """
        Try to retrieve value for the specified name.
        If not available in the current scope, search in parent.
        """
        i = i if i != None else self.index

        if name in self.stack[i]:
            return self.stack[i][name]
        elif i > 0:
            return self.get(name, i - 1)
        else:
            raise NameError(
                "symbol '{}' is not defined"
                .format(name)
            )

    def push(self, bindings=None):
        self.index += 1
        self.stack.append(bindings or {})

    def pop(self):
        self.index -= 1
        self.stack.pop()

    def show(self, exclude=None, include=None):
        for s in self.stack:
            for n, v in s.items():
                if (not include or n in include) and not (exclude and n in exclude):
                    print('    {} - {}'.format(n, v))
