from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
tall = list(map(int, input().split()))
ans = [0 for _ in range(N)]
# print(ans)

for i in range(N):
  target = tall[i]
  # print(i, target, ans)
  zero_cnt = 0
  index = 0
  # print(target, "target")
  while zero_cnt != target:
    if ans[index] == 0:
      zero_cnt += 1
    index += 1
  while ans[index] != 0:
    index += 1
    # print(index, "index")
  ans[index] = i + 1
      


print(*ans)