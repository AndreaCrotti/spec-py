import pytest
import toolz
import voluptuous


# TODO: need a generic function to walk over the dictionary smartly enough
# TODO: should work both on dictionaries and on list of dictionaries

# TODO: have a look at the flatdict library to see if that could be useful as well


def transform(filter_fn, transform_fn, data):
    partial_dict = toolz.valfilter(filter_fn, data)
    rest = toolz.dissoc(data, *partial_dict.keys())
    return toolz.merge(
        rest,
        toolz.valmap(transform_fn, partial_dict),
    )


def traverse(inp, func):
    # TODO: should allow to do transformations in place as well?
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


# TODO: should not output a schema here directly
def to_voluptuous(inp):
    """Given a data structure of any possible shape
    return  a schema that matches everything
    """
    res = {}
    
    for key, val in inp.items():
        if isinstance(val, dict):
            res[key] = {}
            for k, v in val.items():
                res[key][voluptuous.Required(k)] = type(v)
        else:
            res[key] = type(val)

    return voluptuous.Schema(res)
