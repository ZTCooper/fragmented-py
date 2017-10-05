file_name = input('请输入文件名：')
file = open(file_name, 'w')
print('请输入内容【单独输入":w"保存退出】')

while(1):
    content = input()
    if content != ':w':
        file.write(content+'\n')
    else:
        break
    
file.close()
