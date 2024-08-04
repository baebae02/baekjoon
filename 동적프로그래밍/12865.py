N, K = map(int, input().split())

stuff = [[0,0]]
# print(N, K)
dp = [[0] * (N+1) for _ in range(K+1)]
# print(dp)
for i in range(N):
  W, V = map(int, input().split())
  stuff.append([W,V])


for i in range(1, K+1):
  for j in range(1, N+1):
    # print(i, j)
    weight = stuff[j][0]
    value = stuff[j][1]
    if weight > i: # 담을 수 있는 무게보다 더 크다면
      dp[i][j] = dp[i][j-1]
    else: # 더 담을 수 있다면
      dp[i][j] = max(value + dp[i-weight][j-1], dp[i][j-1])

# print(dp)
print(dp[K][N])

