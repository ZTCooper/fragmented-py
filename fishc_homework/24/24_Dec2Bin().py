def Dec2Bin(dec):
    result = ''

    if dec:
        result = Dec2Bin(dec//2)
        return result + str(dec%2)
    else:
        return result

print(Dec2Bin(62))
