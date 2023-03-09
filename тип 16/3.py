F = [1] * (2048 + 1)
for n in range(3, 2048 + 1):
    if n % 2 == 1:
        F[n] = F[n - 1] + n
    else:
        F[n] = F[n - 3] + 2 * n

print(F[2048] - F[2041])
#Ответ: 10229