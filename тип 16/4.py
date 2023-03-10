def F(a, b):
    if a == 0 and b == 0:
        return 0
    elif a >= b and a > 0:
        return F(a - 1, b) + 1
    else:
        return F(a, b - 1) + 1

'''
print(F(10, 20))
print(F(5, 11))
Замечаем, что данная функция возвращает просто a + b
Значит, нужно найти количество пар, таких что a + b = 10**6
Это будут всевозможные пары вида (a, 10**6 - a), где 
a пробегается от 0 до 10**6, то есть 10**6 + 1 пар
'''
print(10**6 + 1)
#Ответ: 1000001

