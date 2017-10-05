def calculate(*nums, base = 3):

    result = 0
    
    for each in nums:
        result += each

    result *= base
    
    print(result)

calculate(2, 3, 4, 5, base = 5)
