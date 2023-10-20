import sys
from CustomFuncs import *

# Задача 1. Напишите программу, которая находит сумму цифр заданного числа. Например, для числа 123 сумма цифр равна 1 + 2 + 3 = 6

num = getNum()

if num < 0 :
    num = abs(num)
res = 0
while num > 0 :
    res += num%10
    num//=10
print(f'Сумма цифр введённого числа равна {res}')

# Задача 2. Вите очень понравилась идея Фёдора с калькулятором, он захотел создать свой, но чтобы не повторять идею друга полностью, решил сделать калькулятор,
#  который перемножает числа от 1 до n. Тем более, у получившегося произведения есть название - факториал. Обозначается он так: n!
# Вводится натуральное число n. Выведи результат умножения чисел от 1 до n.

num = getNum()
if num < 0 :
    print("Введите положительное число!")
    num = getNum()
# elif num == 0 or num == 1 :
#     print('Факториал числа равен 1')
#     sys.exit()
else :
    res = 1
    while num > 1 :
        res *= num
        num -= 1
print(f'Факториал числа равен {res}')


# Задача 3. Миша учит признаки делимости чисел на 7. Чтобы себя проверить, он написал программу, которая выводит все числа, кратные семи до числа n. 
# Есть целое число n. Вывести в столбик все такие числа.

num = getNum()
numDynamic = abs(num)
if -7 < num < 7 :
    print("Таких чисел нет!")
tmp = 7
while tmp <= numDynamic :
    if tmp % 7 == 0 :
        if num > 7 :
            print(tmp)
        else :
            print(-tmp)
    tmp +=1


    
    