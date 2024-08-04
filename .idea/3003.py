li=list(map(int, input().split()))

ans = [1, 1, 2, 2, 2, 8]

for i in range(len(li)):
  print(ans[i]-li[i], end=' ')