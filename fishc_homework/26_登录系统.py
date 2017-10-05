def login():
    print('--- 新建用户：N/n ---')
    print('--- 登录账号：E/e ---')
    print('--- 退出程序：Q/q ---')
    print('\n')

    user_data = {}
    while(1):
        code = input('--- 请输入指令代码：')

        if code == 'N' or code == 'n':
            name = input('请输入用户名：')
            while name in user_data:
                name = input('此用户名已被使用，请重新输入：')
            password = input('请输入密码：')
            user_data[name] = password
            print('注册成功！登录试试！')
            print('\n')

        if code == 'E' or code == 'e':
            name = input('请输入用户名：')
            while name not in user_data:
                name = input('用户名不存在，请重新输入：')
            password = input('请输入密码：')
            if user_data[name] == password:
                print('登录成功！')
            else:
                password = input('密码错误！请重新输入：')
                if user_data[name] == password:
                    print('登录成功！')
            print('\n')

        if code == 'Q' or code == 'q':
            break

    print('--- 程序结束 ---')


login()
