N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))

li = sorted(li)

for i in range(N):
    print(li[i])
