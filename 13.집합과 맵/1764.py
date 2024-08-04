from collections import Counter
N, M = map(int,input().split()) 
noListen = []
noSee = []
for _ in range(N):
    noListen.append(input())
for _ in range(M):
    noSee.append(input())
c = Counter(noListen + noSee)
cnt = 0
ans = []
for i in c:
    if c[i] == 2:
        cnt += 1 
        ans.append(i)
print(cnt)
ans.sort()
for i in ans:
    print(i)
