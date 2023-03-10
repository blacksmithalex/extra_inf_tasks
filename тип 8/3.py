from itertools import *

k = 0
for x in permutations('МАРИНА', r=6):
    s = ''.join(x)
    if s[0] not in 'АИ':
        k += 1
print(k // 2)

#Ответ: 180