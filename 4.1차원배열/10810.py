N, M = map(int, input().split())
li = [0] * N
for i in range(M):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        li[x] = k

print(*li)