import os
all_file = os.listdir(os.path.curdir)

for each_file in all_file:
    print('%s【%dBytes】'% (each_file, os.path.getsize(each_file)))
