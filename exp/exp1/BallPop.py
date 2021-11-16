# 中南大学考研机试题
# 现有a-z26个小球模拟出入栈操作，小球按照a~z的顺序压入栈，在栈顶的元素可以随时被取出，在游戏开始前给出任意26个字母的一些排列，问是否能够由出栈顺序得到这个排列。
a = input()
b = 'abcdefghijklmnopqrstuvwxyz'
l = []
j = 0
i = 0
while i < len(a):
    while (j < len(b)) and (a[i] != b[j]):
        l.append(b[j])
        j = j + 1
    if (j == len(b)): break
    l.append(b[j])
    j = j + 1
    while len(l) != 0 and a[i] == l[len(l)-1]:
        l.pop()
        i = i+1
        if i == len(a): break
if (len(l) == 0):
    print('yes')
else:
    print('no')
