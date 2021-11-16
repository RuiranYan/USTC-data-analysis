# 给出一组字符串，返回其公共前缀


size = int(input())
st = [''] * size
result = ''
if size == 0:
    print(result)
    exit(0)
for i in range(size):
    st[i] = input()
st.sort(key=lambda x: len(x))  # important !!!!!!
for i in range(len(st[0])):
    j = 0
    while j < len(st):
        if st[j][i] != st[0][i]:
            break
        j = j + 1
    if j == len(st):
        result = result + st[0][i]
    else:
        break
print(result)
