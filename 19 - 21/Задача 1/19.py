def f(x, p):
    if x >= 30 and p == 3:
        return True
    elif x < 30 and p == 3:
        return False
    elif x >= 30:
        return False
    else:
        if p % 2 == 0:
            return f(x + 2, p + 1) or f(x + 3, p + 1) or f(x * 2, p + 1)
        else:
            return f(x + 2, p + 1) and f(x + 3, p + 1) and f(x * 2, p + 1)

for S in range(1, 29 + 1):
    if f(S, 1):
        print(S)

#Ответ: 13
