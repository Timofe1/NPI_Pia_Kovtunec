"""Написать функцию, принимающую словарь, который
может содержать любые элементы и конвертирует в Json только те элементы,
значения которых являются списками, содержащими только целочисленные значения """
import json
all_dic = {'a': [1, 2, 3], 'b': [2, '1'], 'c': "Я не список", 'd': 'q', 's': [0]}

def func(arg):
    p = False
    all_date={}
    # isinstance(arg, list)
    for i in arg.items():
        d=0
        if isinstance(i[1], list):
            try:
                for a in i[1]:
                    d = a + d
            except TypeError:
                print(str(i[0])+":"+str(i[1])+" содержит не число\n")
            else:
                all_date.update({i[0]: i[1]})

    with open('bd_laba_5.json', 'w') as f:
        json.dump(all_date, f)



func(all_dic)
with open('bd_laba_5.json') as f:
    print(f.read())


    # with open('bd_laba_5.json') as f:
    #     data = json.load(f)
    #     data.update
    #     with open('bd_laba_5.json', 'w') as outfile:
    #         json.dump(data, outfile)