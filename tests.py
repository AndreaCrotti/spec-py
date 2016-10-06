import pytest
import voluptuous

import spec



def test_select_simple_case():
    inp = {
        "a": {"b": 1},
        "b": {"b": 1},
    }

    assert list(spec.select(inp, ['a', 'b'])) == [1]


def test_simple_maps():
    is_even = lambda n: n % 2 == 0
    inc = lambda n: n + 1

    assert spec.transform(is_even, inc, {'a': 2, 'b': 1}) == {'a': 3, 'b': 1}



@pytest.mark.skip
def test_nested_maps():
    """Increment every number nested within map of vector of maps
    """
    data = {
        'a': [{'aa': 1, 'BB': 2},
              {'cc': 3}],
        'b': [{'dd': 4}],
    }
    desired = {
        'a': [{'aa': 1, 'bb': 3},
              {'cc': 3}],
        'b': [{'dd': 5}],
    }
    is_even = lambda n: n % 2 == 0
    assert spec.transform(is_even, lambda n: n + 1, data) == desired


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
    assert spec.traverse({1: {'a': 2}}, lambda n: n + 1) == {1: {'a': 3}}


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


def test_data_to_voluptuous():
    # given a list of possible input outputs to a certain function
    # generate the minimal matching voluptuous schema
    inp = {'dic': {'a': 1, 'b': 2}}
    desired_schema = voluptuous.Schema({
        'dic': {
            voluptuous.Required('a'): int,
            voluptuous.Required('b'): int,
        }})
    
    # TODO: add check
    spec.to_voluptuous(inp)
    # assert spec.is_isomorphic(spec.to_voluptuous(inp).schema, desired_schema.schema)
    # assert spec.to_voluptuous(inp).schema == desired_schema.schema
