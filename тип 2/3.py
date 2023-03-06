def f(a, b, c):
    return int(a == b or c == b)

print('a b c | f(a, b, c)')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            if f(a, b, c) == 1:
                print(a, b, c, '|', f(a, b, c))
