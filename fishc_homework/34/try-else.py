try:
    temp = int(input('请输入：'))
except ValueError as reason:
    print('出错！' + str(reason))
else:
    print('没有异常')
