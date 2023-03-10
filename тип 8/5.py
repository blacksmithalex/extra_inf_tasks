from itertools import *

k = 0
for x in permutations('0123456789ABCDEF', r=4):
    ch = '02468ACE'
    nch = '13579BDF'
    s = ''.join(x)
    if s[0] != '0' and ((s[0] in ch and s[1] in nch and s[2] in ch and s[3] in nch) or (
            s[0] in nch and s[1] in ch and s[2] in nch and s[3] in ch)):
        k += 1
print(k)

#Ответ: 5880