import toolz


# TODO: need a generic function to walk over the dictionary smartly enough
# TODO: should work both on dictionaries and on list of dictionaries

def transform(inp, filter, func):
    pass


def traverse(inp, func):
    new_result = {}
    # TODO: check how the traverse function in Clojure works
    if not isinstance(inp, dict):
        return func(inp)

    else:
        for key, val in inp.items():
            new_result[key] = traverse(val, func)

    return new_result


def select(dic, path):
    sub_dic = dic.copy()
    is_last = lambda idx: idx == len(path) - 1

    for idx, p in enumerate(path):
        if p in dic:
            if is_last(idx):
                yield sub_dic[p]
            else:
                sub_dic = sub_dic[p]


def test_select_simple_case():
    inp = {
        "a": {"b": 1},
        "b": {"b": 1},
    }
    
    assert list(select(inp, ['a', 'b'])) == [1]


def test_transform():
    inp = {
        1: {"b": 1},
        2: {"b": 1},
    }

    is_even = lambda k: k % 2 == 0
    inc = lambda n: n + 1
    assert transform(inp, filter=is_even, func=inc) == {1: {"b": 1}, 2: {"b": 2}}


def test_traverse():
    func = lambda x: x
    # TODO: test it with more mixed types
    assert traverse({1: 2}, func) == {1: 2}
