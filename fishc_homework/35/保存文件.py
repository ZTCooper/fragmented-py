import easygui as g
import os

path = g.fileopenbox(default = '*.txt')
with open(path) as old_file:
    title = os.path.basename(path)  #去掉路径，返回文件名
    msg = '文件【%s】的内容如下：'% title
    text = old_file.read()
    text_after = g.textbox(msg, title, text)

if text != text_after[:-1]:  #text的返回值会追加一个\n
    choice = g.buttonbox('检测到文件内容发生改变，请选择以下操作：', '警告', ('覆盖保存', '放弃保存', '另存为...'))
    if choice == '覆盖保存':
        with open(path, 'w') as old_file:
            old_file.write(text_after[:-1])
    if choice == '放弃保存':
        pass
    if choice == '另存为...':
        path2 = g.filesavebox(default = '.txt')
        if os.path.splitext(path2)[1] != '.txt':
            path2 += '.txt'
        with open(path2, 'w') as new_file:
            new_file.write(text_after[:-1])
