import datetime
# Напишите функцию, которая берёт на вход строку и возвращает true, если она является палиндромом и false в противном случае.

# def palindrom(message) :
#     reverse = message[::-1]
#     if message == reverse :
#         return True
#     else :
#         return False
    
# print(palindrom(str(input('Введите строку: '))))

# Напишите и вызовете для себя или какого-нибудь персонажа функцию, которая берёт на вход имя, фамилию, отчество и возраст и возвращает строку вида 
# “Иванов Иван Иванович 1973 г.р. зарегистрирован”.

# def info(info) :
#     year = int(datetime.datetime.now().year)
    
#     if len(info) > 4 :
#         print('Информация введена некорректно!')
#     else :
#         try :
#             print(f'{info[0].capitalize()} {info[1].capitalize()} {info[2].capitalize()} {year - int(info[3])} г.р. зарегистрирован')
#         except ValueError :
#             print('Информация введена некорректно!')

# info(input('Введите Фамилию, Имя, Отчество и возраст через пробел: ').split(' '))
        

# Напишите функцию, которая берёт на вход 2 или 3 натуральных числа и возвращает их максимум. 
# Встроенным методом max() пользоваться нельзя Возможно, вам потребуется указать аргумент по умолчанию.

def getMax(nums) :
    try :
        max = int (nums[0])
        for i in range(1, len(nums)) :
            if int(nums[i]) > max :
                max = int(nums[i])
        return max
    except ValueError :
        print('Неверный формат числа!')

print(getMax(input('Введите через пробел числа: ').split(' ')))
