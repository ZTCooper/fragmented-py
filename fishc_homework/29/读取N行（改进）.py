file = input('请输入要打开的文件（E:\\Python\\029文件：一个任务\\test.txt）：')
f = open(file)
count = 0

(start, end) = map(str,input('请输入需要显示该文件的行数【格式如 13:21 或 :21 或 21:】：').split(':'))

if start == '':
    start = 1
if end == '':
    for i in f:
        count += 1
    end = count
    f.seek(0,0)
    #end = len(list(f))
for i in range(int(start)-1):
    f.readline()
for i in range(int(end) - int(start)+1):
    print(f.readline())
