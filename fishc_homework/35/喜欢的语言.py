import easygui as g
import sys

while 1:
    g.msgbox('欢迎进入我的第一个桌面游戏！','你好',ok_button = '开始')

    msg = '你喜欢什么语言？'
    title = '小游戏'
    choices = ('C语言','Python','Ruby')
    
    choice = g.choicebox(msg, title, choices)

    g.msgbox('你的选择是：' +str(choice), '结果')

    msg = '你希望重新开始吗？'
    title = '请选择'

    if g.ccbox(msg, title):     #User chose Continue return 1
        pass
    else:       #User chose Cancel return 0
        sys.exit()
