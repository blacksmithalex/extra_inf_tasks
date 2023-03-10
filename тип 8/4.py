from itertools import *

k = 0
for x in product('0123456789ABCDEF', repeat=5):
    s = ''.join(x)
    if s[0] != '0' and s[0] <= s[1] <= s[2] <= s[3] <= s[4]:
        k += 1
print(k)

#Ответ: 11628