import easygui as g
import os

content = []
path = g.fileopenbox(default = '*.txt')
with open(path) as f:
    title = os.path.basename(path)
    msg = '文件【%s】的内容如下：'% title
    text = f.read()
    g.textbox(msg, title, text)
