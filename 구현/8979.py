N, K = map(int, input().split())
di = {}
for i in range(N):
  k, gold, silver, bronze = map(int, input().split())
  di[k] = gold * 10000000 + silver * 100000 + bronze
val = di[K]

di = sorted(di.items(), key=lambda x : (-x[1]))
print(di)

cnt = 0
for k in di:
  if k[1] > val:
    cnt +=1 
  else:
    break

print(cnt+1)