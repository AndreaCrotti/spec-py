import toolz
from functools import wraps
from collections import defaultdict, namedtuple

from spec import to_voluptuous

result = defaultdict(list)

Trace = namedtuple('Trace', ['ret', 'args', 'kwargs'])


def collector(func):
    @wraps(func)
    def _collector(*args, **kwargs):
        ret = func(*args, **kwargs)
        result[func].append(Trace(ret=ret, args=args, kwargs=kwargs))
        return ret

    return _collector


def reduce_schema(result):
    for func, vals in result.items():
        # schema_return = map(to_voluptuous, [{'__return__': x.ret} for x in vals])
        return to_voluptuous({'__return__': vals[0].ret})
        # if set(schemas) != schemas:
        # print("Mismatching schemas {}".format(vals))
        # else:
        return list(schemas)[0]


@collector
def simple_addition(a, b):
    return a + b
