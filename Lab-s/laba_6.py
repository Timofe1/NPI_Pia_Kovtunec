"""Написать функцию, которая принимает наименование
таблицы и выводит количество одинаковых значений в её полях и наиболее часто повторяющееся значение полей. """
import sqlite3
import string
import random
import os
all_list=[]
all_dict={}
max= 0
# # #########____________________________________________________________ Создание базы  masters/ numbers
# connection = sqlite3.connect('db_laba_6_0.2.db')
#
# cursor = connection.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS masters (
#     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#     number INTEGER NOT NULL,
#     nonumber STRING NOT NULL
# )""")
# print("успех")
# connection.commit()
# cursor.close()

abc = string.ascii_letters
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


# ____________________________________________________________Заполнение базы
# with sqlite3.connect("db_laba_6_0.2.db") as con:
#     cur = con.cursor()
#     for i in range(100):
#         s = random.choice(abc)
#         point = (42, s)
#         cur.execute("""INSERT INTO masters
#                          (number, nonumber)
#                          VALUES
#                          (?,?)""",point)


d = int(input("Введите число работы 1-да 0-нет:"))
if d == 1:
    def func(namebase):

        with sqlite3.connect('db_laba_6_0.2.db') as con:
            cur = con.cursor()
            t = ("SELECT * FROM "+namebase)
            cur.execute(t)
            all_numbers_db = cur.fetchall()
        print(all_numbers_db)
        return all_numbers_db

    choice_base = int(input("numbers > 1      masters > 2   >:"))

    if choice_base == 1:
        all_numbers = func('numbers')
    elif choice_base == 2:
        all_numbers = func('masters')

    for i in all_numbers:
        all_list.extend(i)

    for i in all_list:
        counter = all_list.count(i)

        if counter > 1:
            all_dict.update({i:counter})

    for i in all_dict.items():
        if max < i[1] and i[1] < 100:
            max = i[1]
            i_list = i[0]


    print("\n")
    print(all_list)

    print("\n")
    print(all_dict)


    print("\n")

    print(str(i_list)+":"+str(all_dict[i_list]))
    limit = 2
    while(limit > -1):
        limit = int(input("Нижняя граница повторений: >"))

        for i in all_dict.items():
             if i[1]>=limit:
                  print(str(i[0]) + ":" + str(i[1]))