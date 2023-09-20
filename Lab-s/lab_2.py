""" Написать функцию, которая принимает список списков
и с помощью генератора выражения создает и возвращает новый список, который содержит все элементы входящих списков """

x = [[1, 2, 3], [4, 5, 6]]
print(x)
print("\n")
def genlist(xx):
    lll=[]
    for i in xx:
        lll.extend(i)
    yield lll

def func(arg):

        g = genlist(arg)
        print(g)
        print(next(g))

func(x)