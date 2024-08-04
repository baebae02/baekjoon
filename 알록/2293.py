N, K = map(int, input().split())
coin = []
for _ in range(N):
  coin.append(int(input()))

DP = [0] * (K + 1)
DP[0] = 1
for c in coin:
    for i in range(c, K + 1):
        print(c, i, DP)
        DP[i] += DP[i - c]

print(DP[K])