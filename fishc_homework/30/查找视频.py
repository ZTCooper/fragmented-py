import os

def search_file(search_dir, target = ('.mp4', '.rmvb', '.avi')):

    os.chdir(search_dir)
    
    all_file = os.listdir(os.curdir)
    
    for each_file in all_file:
        file_type = os.path.splitext(each_file)[1]
        
        if file_type in target:
            file_list.append(os.getcwd() + os.sep + each_file + os.linesep)
            
        if os.path.isdir(each_file):
            search_file(each_file)
            os.chdir(os.pardir)

    return file_list
            
curdir = os.getcwd()
file_list = []
search_dir = input('请输入待查找的目录：')
video_list = search_file(search_dir, target = ('.mp4', '.rmvb', '.avi'))
f = open(curdir + os.sep + 'videoList.txt', 'w')
f.writelines(video_list)
f.close()
