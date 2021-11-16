# 判断某一年是否是闰年
a = int(input())
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('yes')
else:
    print('no')
