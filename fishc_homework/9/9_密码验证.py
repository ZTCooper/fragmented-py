
key = "123456"
count = 3

while count != 0:
    password = input("请输入密码：")
    if password == key:
        print("密码正确！正在进入程序......")
        break
    
    elif '*' in password:
            print("密码中不包含‘*’，你还有"+str(count)+"次机会！\n")
            continue
    else:
        print("密码错误！")
        count -= 1
        print("你还有"+str(count)+"次机会！\n")
        
    
        
            
