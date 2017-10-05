file = input('请输入要打开的文件（E:\\Python\\029文件：一个任务\\test.txt）：')
n = int(input('请输入需要显示该文件前几行：'))

f = open(file)

print('文件',file,'的前',n,'行内容如下：\n')
for i in range(n):
    print(f.readline())

f.close()
