import toolz


# TODO: need a generic function to walk over the dictionary smartly enough

def transform(inp, filter, func):
    pass


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
