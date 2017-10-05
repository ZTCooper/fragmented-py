def sum(x):
    
    result = 0
    
    for each in x:
        if isinstance(each, int) or isinstance(each, float):
            result += each
        else:
            continue

    return result

print(sum([1,2,3.4,'a','4']))
