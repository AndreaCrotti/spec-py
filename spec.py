import toolz


def select(dic, path):
    sub_dic = dic.copy()
    for idx, p in enumerate(path):
        if p in dic:
            sub_dic = dic[p]
            

def test_long_name():
    inp = {
        "a": {"b": 1},
        "b": {"b": 1},
    }
    
    assert list(select(inp, ['a', 'b'])) == [1]
