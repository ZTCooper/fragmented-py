# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位

symbols = r'~!@#$%^&*()_=-/,.?<>;:[]{}|'
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'

password = input('请输入密码：')
length = len(password)

if password.isspace() or length == 0:
    password = input('密码为空，请重新输入：')
    
#密码长度
    
if length <= 8:
    flag_len = 1

elif 8 < length < 16:
    flag_len = 2

else:
    flag_len = 3

#判断包含字符

flag_con = 0

for each in password:
    if each in symbols:
        flag_con += 1
        break

#判断包含字母

for each in password:
    if each in chars:
        flag_con += 1
        break

#判断包含数字

for each in password:
    if each in num:
        flag_con += 1
        break

#打印结果

print('您的密码安全等级评定为：',end = '')

if flag_len == 1 or flag_con == 1:
    print("低")

elif flag_len == 2 or flag_con == 2:
    print("中")

elif flag_len == 3 or flag_con == 3:
    print("高")
