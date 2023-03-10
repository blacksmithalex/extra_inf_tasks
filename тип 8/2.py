from itertools import *

k = 0
for x in product('012345678', repeat=7):
    s = ''.join(x)
    p = True
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2] or s[0] == '0' or s[-1] in '347':
            p = False
    if p:
        k += 1
print(k)
#Ответ: 2676053 