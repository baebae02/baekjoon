T = int(input())

dp = [0, 1, 2, 4, 7]
for _ in range(T):
  N = int(input())
  for i in range(len(dp), N+1):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])
  print(dp[N])