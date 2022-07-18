N = int(input())
li = []
for i in range(N):
    x, y = map(int, input().split())
    li.append([x,y])
li.sort()

for i in li:
    print(*i)
