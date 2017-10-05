def palindrome(string):
    list1 = list(string)
    list2 = reversed(list1)
    if list1 == list(list2):
        return '是回文'
    else:
        return '不是回文'

print(palindrome('上海自来水来自海上'))
