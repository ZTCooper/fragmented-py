f = open(r'E:\Python\029文件：一个任务\对话.txt')

mom = []
baby = []
count = 1

def divide():
        file_name_mom = 'mom_' + str(count) + '.txt'
        file_name_baby = 'baby_' + str(count) + '.txt'

        mom_file = open(file_name_mom, 'w')
        baby_file = open(file_name_baby, 'w')

        mom_file.writelines(mom)
        baby_file.writelines(baby)

        mom_file.close()
        baby_file.close()

for each_line in f:
    if each_line[:6] != '======':
        (role, line_spoken) = each_line.split('：',1)
        if role == '妈妈':
            mom.append(line_spoken)
        if role == '宝宝':
            baby.append(line_spoken)

    else:
        divide()

        mom = []
        baby = []
        count += 1

divide()

f.close()
