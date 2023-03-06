def f(x, y, z, w):
    l1 = x <= y
    l2 = z <= w
    l3 = z == y
    l4 = w == x
    return int((l1 or l2) and (l3 <= l4))

print('x y z w | f(x, y, z, w)')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if f(x, y, z, w) == 0:
                    print(x, y, z, w, '|', f(x, y, z, w))
