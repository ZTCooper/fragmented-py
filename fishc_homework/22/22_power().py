def power1(x, y):
    if y == 0:
        return 1
    else:
        return x * power1(x, y - 1)

#i = input('请输入两个数：')
x, y = map(int, input('请输入两个数：').split())
print(power1(x,y))
