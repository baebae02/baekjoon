N, M = map(int, input().split())
pocketMon = {}
Q = []
for i in range(N):
    pocketMon[i+1] = input()
rv = {v:k for k,v in pocketMon.items()}

for _ in range(M):
    q = input()
    if q[0] >= 'A':
        print(rv.get(q))
    else:
        print(pocketMon.get(int(q)))
