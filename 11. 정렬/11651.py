N = int(input())
li = []
for i in range(N):
    x, y = map(int, input().split())
    li.append([y,x])
li.sort(reverse=False)

for i in range(N):
    li[i][0], li[i][1] = li[i][1], li[i][0]
for i in li:
    print(*i)
