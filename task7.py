from functools import reduce

# Задача 1. Напишите программу на Python для поочередного сложения элементов двух заданных списков, используя map и lambda.

# list1 = [1, 2, 3, 4, 5]
# list2 = [1, 2, 3, 4, 5]
# print(list(map(lambda a, b : a + b, list1, list2)))

# Задача 2. Напишите программу на Python для поиска чисел из списка, кратных девятнадцати или тринадцати, используя filter и  Lambda.

# list1 = [24, 2, 26, 4, 169]
# print(list(filter(lambda num: num % 12 == 0 or num % 13 == 0, list1 )))

# Задача 3. Напишите программу на Python для вычисления наибольшего элемента в списке при помощи reduce

list1 = [240, 2, 26, 4, 169]

print(reduce(lambda a, b: a if a > b else b, list1))