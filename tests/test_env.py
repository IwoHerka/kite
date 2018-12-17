from archaeopteryx.env import Environment


def test_env_set_get():
    env = Environment()

    o = object()
    env.set('a', 1)
    env.set('b', o)

    assert env.get('a') == 1
    assert env.get('b') == o


def test_env_override_global():
    env = Environment()
    env.set('a', 1)
    env.push()
    env.set('a', 2)

    assert env.get('a') == 2
    env.pop()
    # Poping level should have no effect
    # on `a`, because current level
    # did not shadow it.
    assert env.get('a') == 2


def test_env_introduce_local():
    env = Environment()
    env.set('a', 1)
    env.push({'a': 2})

    assert env.get('a') == 2
    env.pop()
    assert env.get('a') == 1
