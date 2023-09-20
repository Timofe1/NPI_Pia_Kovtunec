"""Написать функцию, которая принимает два словаря и
возвращает новый словарь, в котором значения одинаковых
ключей из входящих словарей являются суммой, а разные ключи просто добавляются в
новый словарь. Например, для

входящих словарей {‘a’:200, ‘b’:50} и {‘a’:100, ‘c’:500}

выходным словарем {‘a': 300, ‘b’:50, ‘c’:500}
"""
dict_o = {'a': 200, 'b': 100}
dict_s = {'a': 100, 'd': 10, 'b': 50, 'c': 10}
dict_a = {}
l_view = []
def func(arg_o: dict, atg_s: dict):
    l_list = []
    dict_la ={}
    keys_o = sorted(arg_o.keys())
    keys_s = sorted(atg_s.keys())
    l_list.extend(keys_s)
    l_list.extend(keys_o)
    l_list.sort()
    for x in range(len(l_list)):
        a = x+1
        if (a < len(l_list)):
            if l_list[x] == l_list[x+1]:
                l_list.pop(x)
    print(l_list)
    for i in l_list:
        a = arg_o.get(i)
        b = atg_s.get(i)
        if (a!=None and b!=None):
            suma = a + b
            dict_la.update({i: suma})
        elif a == None:
            dict_la.update({i: b})
        elif b == None:
            dict_la.update({i: a})
    return dict_la

dict_a.update(func(dict_o, dict_s))
print(dict_a)