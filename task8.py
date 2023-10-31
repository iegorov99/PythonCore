# Напишите рекурсивную функцию, которая находит максимальное число в заданном списке. 
# Программа должна работать для любого количества чисел. Встроенную функцию max() использовать нельзя. 

# string = input('Введите через пробел числа: ').split(' ')
# nums = []

# try :
#     for letter in string :
#         nums.append(int(letter))
# except ValueError :
#     print('Введено неверное значение!')
nums = [1 ,2 ,3 ,4 ,5]

def getMax(nums, max = None) :
    if max == None :
        max = nums.pop()
    currnet = nums.pop()
    if currnet > max :
        max = currnet
    if nums :
        return getMax(nums, max)
    return max

print(getMax(nums))