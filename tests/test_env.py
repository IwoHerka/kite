from archaeopteryx.env import Environment


def test_env_set_get():
    env = Environment()

    o = object()
    env.set('a', 1)
    env.set('b', o)

    assert env.get('a') == 1
    assert env.get('b') == o


def test_env_parent_relation():
    par = Environment({'a': 1})
    env = Environment(parent=par)

    assert env.get('a') == 1

    env.set('a', 2)
    assert env.get('a') == 2
