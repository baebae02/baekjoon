from collections import Counter
xl = []
yl = []
for _ in range(3):
    x, y = map(int,input().split())
    xl.append(x)
    yl.append(y)

xc = Counter(xl)
yc = Counter(yl)
for x in xc:
    if xc[x] == 1:
        print(x, end=' ')

for y in yc:
    if yc[y] == 1:
        print(y)
