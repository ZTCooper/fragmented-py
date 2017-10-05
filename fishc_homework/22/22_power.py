def gcd1(x, y):
    if x % y == 0:
        return y
    else:
        return gcd1(y, x % y)

x, y = map(int, input('请输入两个数：').split())
print(gcd1(x,y))
