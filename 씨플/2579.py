import sys
input = sys.stdin.readline
stair_n = int(input())
DP = [0] * 301  # DP = [0] * (stair_n + 1)
stair = [0] * 301 # stair = [0]
for i in range(1, stair_n + 1):
    stair[i] = int(input()) # stair.append(int(input()))

# print(stair)

DP[1] = stair[1]
DP[2] = stair[2] + stair[1]
DP[3] = max(stair[1] + stair[3], stair[2] + stair[3])
for i in range(4, stair_n + 1):
  DP[i] = max(DP[i-3] + stair[i-1] + stair[i], DP[i-2] + stair[i])

# print(DP)
print(DP[stair_n])