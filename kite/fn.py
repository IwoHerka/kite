from .list import List
from .symbol import F, Symbol, T
from .num import Integer, Float, Rational


class Lambda:
    def __init__(self, symbols, form):
        self.names = tuple([s.name for s in symbols])
        self.form = form

    def __str__(self):
        return '(lambda {} {})'.format(
            ' '.join(self.names),
            str(self.form)
        )

    def eval(self, env, args):
        if len(args) != len(self.names):
            raise TypeError(
                'Wrong number of arguments, expected: {}, got: {}'
                .format(len(self.names), len(args))
            )

        bindings = dict(zip(self.names, args))
        env.push(bindings)
        retval = F

        for f in self.form:
            retval = f.eval(env)

        env.pop()
        return retval


class Function:
    def __init__(self, fn):
        self.fn = fn

    def __str__(self):
        return str(self.fn.__doc__)

    def eval(self, env, args):
        return self.fn(env, args)


def atom(env, args):
    """Atom has the value of 't' or 'f' according to
    whether its argument is an atomic symbol. Thus:

        (atom t) = t
        (atom (quote (t f))) = f
    """
    arg = args.car().eval(env)

    if isinstance(arg, Symbol) or arg == F:
        return T

    return F


def car(env, args):
    """Returns head of the list. Car is
    defined if and only if its argument is not atomic:

        (car (quote (e1 e2))) = e1
    """
    return args.car().eval(env).car()


def cdr(env, args):
    """Returns body of the list. Cdr is
    defined if and only if its argument is not atomic:

        (cdr (quote (e1 e2))) = (e2)
    """
    return args.car().eval(env).cdr()


def cond(env, args):
    for expr in args:
        if expr.car().eval(env) == T:
            return expr.cdr().car().eval(env)

    return F


def cons(env, args):
    """For any x and y, constructs a list (x, y).
    """
    if len(args) != 2:
        raise TypeError(
            "Function 'cons' expects two arguments, got: {}"
            .format(args)
        )
    else:
        return args.cdr().car().eval(env).cons(args.car().eval(env))


def eq(env, args):
    """If x and y are atomic, return 't' if x are y
    are equal, otherwise 'f'.
    """
    lhs = args.car().eval(env)
    rhs = args.cdr().car().eval(env)

    if not (type(lhs) is Symbol and (type(rhs) is Symbol or rhs == F)):
        raise TypeError(
            "Function 'eq' if defined only for symbols, got: {}, {}"
            .format(lhs, rhs)
        )
    else:
        return T if lhs == rhs else F


def quote(env, args):
    """Returns its argument; stops evaluation:

        (quote (1 2 3)) = (1 2 3)
    """
    if len(args) > 1:
        raise ValueError(
            "Function quote expectes one argument, got: '{}'"
            .format(args)
        )
    else:
        return args.car()


def lambda_(env, args):
    return Lambda(args.car(), args.cdr().car())


def label(env, args):
    """Assigns expression to a name. Example:

        (label even (lambda (x) (= (/ x 2.0) 0)))
        (even 4)
    """
    if len(args) != 2:
        raise TypeError(
            "'label' expects two arguments, got: {}"
            .format(args.car(), args.cdr())
        )
    else:
        if not type(args.car()) is Symbol:
            raise TypeError(
                "'label' expects a symbol as the first argument, got: {}"
                .format(args.car())
            )

        name = args.car().name
        env.set(name, args.cdr().car().eval(env))
        return env.get(name)


def add(env, args):
    lhs = args.car().eval(env)
    rhs = args.cdr().car().eval(env)

    if (
        isinstance(lhs, (Integer, Float, Rational))
        and isinstance(lhs, (Integer, Float, Rational))
    ):
        return lhs.add(rhs)
    else:
        raise TypeError()


