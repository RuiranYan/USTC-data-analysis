# 求100以内的全部素数
frag = [1] * 100
a = [0] * 100
frag[0] = 0
for i in range(100):
    a[i] = i + 1
for i in range(1,100):
    if frag[i] == 1:
        for j in range(i+1, 100):
            if a[j] % a[i] == 0:
                frag[j] = 0
for i in range(100):
    if frag[i] == 1:
        print(a[i], end=' ')
