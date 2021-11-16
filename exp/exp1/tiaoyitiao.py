# 西安电子科技大学2018考研复试计算机类上机试题
# 前一段时间在微信中很火的跳一跳游戏规则如下：短跳得1分，跌落则游戏结束，长跳得2分，并且长跳可连续累加，第一次2分，第二次4分，依次类推，若长跳中断则重新计分2分。现给定0,1,2的组合序列，其中0：跌落 1：短跳成功 2：长跳成功。请你计算玩家当次游戏的合计得分。


size = int(input())
l = list(map(int, input().split(" ")))
s = 0
front = 0
for i in range(len(l)):
    if (l[i] == 0):
        break
    elif (l[i] == 1):
        s = s + 1
        front = 0
    else:
        front = front + 2
        s = s + front
print(s)