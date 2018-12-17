class Environment:
    def __init__(self, names=None, parent=None):
        self.names = names or {}
        self.parent = parent

    def set(self, name, val):
        """
        Assign value to a name. By default, names will be
        stored in the lowest scope possible.
        """
        # To avoid uncesessary stack traversal,
        # always check if name is available locally first.
        if name in self.names:
            self.names[name] = val
        # Only if not, check the parent.
        elif self.parent:
            self.parent.set(name, val)
        # Finally, if name is unknown, assign it
        # at the current level.
        else:
            self.names[name] = val

    def get(self, name):
        """
        Try to retrieve value for the specified name.
        If not available in the current scope, search in parent.
        """
        if name in self.names:
            return self.names[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            raise NameError(
                "symbol '{}' is not defined"
                .format(name)
            )

    def push(self, names=None):
        """Create new scope with current enviornment as parent."""
        return Environment(name, parent=self)

    def pop(self):
        """Return previous scope."""
        return self.parent
