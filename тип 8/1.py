from itertools import *

k = 0
for x in product('МЕТРО', repeat=4):
    s = ''.join(x)
    if s[0] in 'МТР' and s[-1] in 'ЕО':
        k += 1
print(k)

#Ответ: 150 