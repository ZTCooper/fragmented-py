file = input('请输入文件名：')
old_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')

count = 0
content = []

f = open(file)
for each_line in f:
    if old_word in each_line:
        count += each_line.count(old_word)
        each_line = each_line.replace(old_word,new_word)
    content.append(each_line)
f.close()

print('文件',file,'中共有',count,'个【',old_word,'】')
print('您确定要把所有的【',old_word,'】替换为【',new_word,'】吗？')

YN = input('【YES/NO】')
if YN == 'YES':
    f = open(file,'w')
    f.writelines(content)

f.close()

