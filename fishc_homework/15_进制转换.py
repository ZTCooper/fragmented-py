q = True
while q:
    num = input('请输入一个十进制整数（输入Q结束程序）：')
    if num != 'Q':
        num = int(num)
        print('十进制 -> 二进制：%d -> ' % num, bin(num))
        print('十进制 -> 八进制：%d -> 0%o' % (num, num))
        print('十进制 -> 十六进制：%d -> 0x%x' % (num, num))
        print('\n')
    else:
        q = False
