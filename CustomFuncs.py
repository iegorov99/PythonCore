def getNum(message) :
    try :
        a = int(input(message))
        return a
    except ValueError :
        print('Это не число!')

def isAnagram(message1, message2) :
    for letter in message1, message2 :
        if letter == ' ' :
            message1 = message1.replace(letter, '')
            message2 = message2.replace(letter, '')
    
    if len(message1) != len(message2) :
        return False
    dict = {}

    for i in range(len(message1)) :
        dict[message1[i]] = dict.get(message1[i], 0) + 1

    for i in range(len(message2)) : 
        if not message2[i] in dict:
            return False
        dict[message2[i]] = dict[message2[i]] - 1
        if dict[message2[i]] == 0:
            del dict[message2[i]]
    return not dict

def addStudent(studentsAll, group1, group2, group3) :
    for student in group1 :
        if student not in studentsAll :
            studentsAll.append(student)
    
    for student in group2 :
        if student not in studentsAll :
            studentsAll.append(student)

    for student in group3 :
        if student not in studentsAll :
            studentsAll.append(student)