import pytest
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


def is_isomorphic(d1, d2):
    with_types_1 = traverse(d1, lambda v: type(v))
    with_types_2 = traverse(d2, lambda v: type(v))
    return with_types_1 == with_types_2

