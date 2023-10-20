def getNum() :
    try :
        a = int(input('Введите число: '))
        return a
    except ValueError :
        print('Это не число!')