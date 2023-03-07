file = open('9-3.txt')
count = 0
for line in file:
    nums = sorted([int(x) for x in line.split()])
    if len(set(nums)) == 6:
        avg = sum(nums) / 6 # среднее значение
        mid = (nums[2] + nums[3]) / 2 # медиана
        if avg >= mid:
            count += 1
print(count)
#Ответ: 2097
