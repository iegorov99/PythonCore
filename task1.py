# Написать программу, которая будет округлять число до заданного количества знаков после запятой

try : 
    num = float(input("Введите число: "))
    ndigits = int(input("Введите количество знаков после запятой: "))
    print(round(num, ndigits))
except ValueError :
    print("Введено неверное значение!")

# Написать программу, которая будет находить среднее арифметическое двух чисел и округлять его до целого числа.

try :
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print(round((num1+num2)/2))
except ValueError :
    print("Введено неверное значение!")
