from itertools import product
from math import sqrt
def odd_count(x):
    count = 0
    for l in x:
        if int(l) % 2 == 0:
            count += 1
    return count
def is_prime(x):
    if x == 1:
        return False
    for d in range(2, int(sqrt(x)) + 1):
        if x % d == 0:
            return False
    return True

nums = list('0123456')
count = 0
for x in product(nums, repeat = 5):
    if x[0] == '0':
        continue
    x = ''.join(x)
    s = sum([int(l) for l in x])
    if odd_count(x) >= 3 and is_prime(s):
        count += 1
print(count)
