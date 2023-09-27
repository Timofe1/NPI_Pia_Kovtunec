"""Написать функцию,
которая принимает список, который содержит строки и выводит на экран новые списки из входящих строк"""

one_list = ['abc', 'абв' ]
print ("Список со строками")
print (one_list)
def func(arg):
    sec_list = []
    for i in arg:
        sec_list.append([i])
    print ("Список списков со строками")
    print(sec_list)

func(one_list)