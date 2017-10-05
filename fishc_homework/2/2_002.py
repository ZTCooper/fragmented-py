print('--------猜猜小游戏---------')
temp = input("不妨猜一下我现在心里想的是哪个数字：")
guess = int(temp)
if guess == 8:
    print("猜对了！")
    print("那也没有奖励！")
else:
    print("猜错啦，我想的是8！")
print("游戏结束！")
