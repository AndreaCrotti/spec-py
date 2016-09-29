import pytest

from spec import spec


def test_select_simple_case():
    inp = {
        "a": {"b": 1},
        "b": {"b": 1},
    }

    assert list(spec.select(inp, ['a', 'b'])) == [1]


def test_transform():
    inp = {
        1: {"b": 1},
        2: {"b": 1},
    }

    is_even = lambda k: k % 2 == 0
    inc = lambda n: n + 1
    # assert transform(inp, filter=is_even, func=inc) == {1: {"b": 1}, 2: {"b": 2}}


def test_traverse():
    func = lambda x: x
    # TODO: test it with more mixed types
    assert spec.traverse({1: 2}, func) == {1: 2}


@pytest.mark.parametrize(('inp', 'out'), [
    ({'a': 1}, {'a': 2}),
    # TODO: None should work
])
def test_is_isomorphic(inp, out):
    assert spec.is_isomorphic(inp, out)


@pytest.mark.parametrize(('inp', 'out'), [
    ({'a': 1}, {'b': 2}),
    ({'a': 1}, {'a': 2, 'b': 1}),  # extra key on the right
    ({'a': 1, 'b': 1}, {'a': 2}),  # extra key on the left
    ({'a': 1}, {'a': 'type'}),  # mismatching type
])
def test_is_not_isomorphic(inp, out):
    assert not spec.is_isomorphic(inp, out)
