year = input("请输入年份：")
year = int(year)
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("是闰年！")
else:
    print("不是闰年！")
