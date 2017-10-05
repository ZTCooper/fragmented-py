
for num in range(100,1000):
    if num == (num % 10) ** 3 + (num // 10 % 10) ** 3 + (num // 100) ** 3:
        print(num)
'''
for i in range(100, 1000):
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp%10) ** 3
        temp //= 10
    if sum == i:
        print(i)

'''
