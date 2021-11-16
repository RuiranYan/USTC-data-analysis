# 西安电子科技大学2018考研复试
# 给定一组条数为n(n<100)的记录，记录了小明各个时期的考试成绩 ，格式为日期+成绩，中间以空格隔开，记录之间分行输入，例如：
# 2008/6/3 80
# 2009/1/1 56
# …
# 其中日期输入要求年份1996-2100，月份1-12，日期1-31。
# 现要求以分数为关键字从大到小对其进行排序，若分数相同则按日期从小到大排序。
import re

size = int(input())
st = [''] * size
l = []
for i in range(size):
    st[i] = input()
    st[i] = re.split('/| ', st[i])
    li = (int(st[i][3]), int(st[i][0]), int(st[i][1]), int(st[i][2]))
    l.append(li)
l.sort(key=lambda x: (-x[0], x[1], x[2], x[3]))
for i in range(size):
    print("%d/%d/%d %d" % (l[i][1], l[i][2], l[i][3], l[i][0]))
