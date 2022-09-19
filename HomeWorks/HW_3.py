# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(*my_list[2])
#print(my_list[2])

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# summa = 0
# for i in list_1:
#     if type(i) == int:
#         summa += i
#     elif type(i) == str and 'a' in i:
#         print(i)
# print(summa)

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# print('Original list: ', list_1)
# print('Sum of all numbers: ', sum([x for x in list_1 if type(x) == int ]))
# print('All words with a: ', [y for y in list_1 if type(y) == str and "a" in y])


# 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
# list_2 = ['cat', 'dog', 'horse', 'cow']
# my_tuple = tuple(list_2)
# print(type(my_tuple))

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
#
# family_1 = input('Введите членов 1й семьи через , :')
# family_2 = input('Введите членов 2й семьи через , :')
# f1 = family_1.split(',')
# f2 = family_2.split(',')
# if len(f1) > len(f2):
#     print('Семья 1 больше')
# elif len(f2) > len(f1):
#     print('Семья 2 больше')
# elif len(f1) == len(f2):
#     print('Equal')

# print("Equal" if len(family_1) == len(family_2) else family_2 if len(family_2) > len(family_1) else family_1)


# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
#
# film = {'title': 'Siberiada',
#         'director': 'Andrey Konchalovsky',
#         'year': 1978,
#         'budget':'1$',
#         'main_actor': 'Ludmila Gurchenko',
#         'slogan': 'В сибирской глухомани'
#         }
# print(film.keys())
# print(film.values())
# print(film.items())

# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# summa = sum(my_dictionary.values())
# print(summa)
#

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# my_list = [1, 2, 3, 4, 5, 3, 2, 1]
# my_list1 = []
# for i in my_list:
#     if i not in my_list1:
#         my_list1.append(i)
# print(my_list1)

#
# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#
# print(set2.intersection(set1))
# print(set2.difference(set1), set1.difference(set2))
#
# print(set1.issubset(set2))
# print(set2.issubset(set1))


