"""Написать функцию, которая принимает путь к
директории и наименование файла и
возвращает полный путь к полученному файлу """
from tkinter import filedialog as fd


filename = fd.askopenfilename()
print(filename)



# dir = str(input("Введите путь к директории:"))
# name_file = str(input("Введите наименование файла:"))
# def func(o_arg,s_srg):
#     print(o_arg+s_srg)

# func(dir,name_file)