N = int(input())

DP = [0] * (N + 1)
DP[0] = 1
if N >= 2:
  DP[2] = 3

for i in range(4, N+1, 2):
  DP[i] = DP[i-2] * 3
  for j in range(0, i-2, 2):
    print(i, j, DP)
    DP[i] += DP[j] * 2

print(DP[N])