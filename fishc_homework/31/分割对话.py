import pickle

def save_file(mom, baby, count):
        mom_name_file = 'mom_'+str(count)+'.txt'
        baby_name_file = 'baby_'+str(count)+'.txt'

        mom_file = open(mom_name_file, 'wb')
        baby_file = open(baby_name_file, 'wb')

        pickle.dump(mom, mom_file)
        pickle.dump(baby, baby_file)

        mom_file.close()
        baby_file.close()
        
def split_file(file_name):
    mom = []
    baby = []
    count = 1

    f = open(r'E:\Python\029文件：一个任务\对话.txt')
    for each_line in f:
        
        if each_line[:6] != '======':
            (role, line_spoken) = each_line.split('：',1)
            if role == '妈妈':
                mom.append(line_spoken)
            if role == '宝宝':
                baby.append(line_spoken)


        else:
            save_file(mom, baby, count)

            mom = []
            baby = []
            count += 1

    save_file(mom, baby, count)
    f.close()

split_file('对话.txt')
