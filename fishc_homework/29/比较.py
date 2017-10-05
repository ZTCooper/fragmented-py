file1 = input('请输入需要比较的头一个文件名：')
file2 = input('请输入需要比较的另一个文件名：')

count = 0 #统计行数
differ = [] #统计不一样的数量
f1 = open(file1)
f2 = open(file2)

for line1 in f1:
    line2 = f2.readline()
    count += 1
        
    if line1 != line2:
        differ.append(count)
            
print('两个文件共有【%d】处不同' % len(differ))
for i in differ:
    print('第%d行不一样' % i)
