'''
member = ['Lucy', 88, 'Lily', 90, 'Adam', 85]
for each in member:
    print(each)
'''
'''
member = ['Lucy', 88, 'Lily', 90, 'Adam', 85]
count = 0
length = len(member)
while count < length:
    print(member[count], member[count+1])
    count += 2
'''

member = ['Lucy', 88, 'Lily', 90, 'Adam', 85]
for each in range(len(member)):
    if each % 2 ==0:
        print(member[each], member[each+1])
