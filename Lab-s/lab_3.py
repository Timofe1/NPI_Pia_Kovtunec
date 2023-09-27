""" Написать функцию, которая принимает список списков
и с помощью генератора выражения создает и возвращает новый список, который содержит все элементы входящих списков """

list_list = [[1, 2, 3], [4, 5, 6]]
print(list_list)
print("\n")

def genlist(arg):
    lll=[]
    for i in arg:
        lll.extend(i)
    yield lll


def func(arg):
        g = genlist(arg)
        print(g)
        print(next(g))
func(list_list)