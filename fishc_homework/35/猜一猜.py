import easygui as g
import sys
import random

while 1:
    g.msgbox('开始游戏吧！','猜一猜','开始')

    guess = g.integerbox('不妨猜一下我现在心里想的是哪个数字(1—10)','数字小游戏',lowerbound = 1, upperbound = 10)
    answer = random.randint(1,10)

    if guess == answer:
        g.msgbox('猜对了！','恭喜你')
    else:
        g.msgbox('猜错了，答案是%d'%answer, '很遗憾')

    cc = g.ccbox('想要再试一次吗？', '请选择',('再一次！','告辞！'))
    if cc:
        pass
    else:
        sys.exit()
