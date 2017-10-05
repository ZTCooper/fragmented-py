str1 = input('请输入字符串：')
countA = 0
countB = 0
countC = 0
length = len(str1)

for i in range(length):
    if str1[i] == '\n':
        continue
    
    if str1[i].isupper():
        if countB == 1:
            countC += 1
            countA = 0
        else:
            countA += 1
        continue
    
    if str1[i].islower() and countA == 3:
        countB = 1
        countA = 0
        target = i
        continue

    if str1[i].islower() and countC == 3:
        print(str1[target],end = '')
        
    countA = 0
    countB = 0
    countC = 0
