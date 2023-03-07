file = open('9-1.txt')
count = 0
for line in file:
    a, b, c, d = sorted([int(x) for x in line.split()])
    if (d - a) >= 50 and b * c <= 1000:
        count += 1
print(count)

#Ответ: 423
