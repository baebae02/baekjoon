from sys import stdin
input = stdin.readline

N = int(input())
num = []
for _ in range(N):
  num.append(int(input()))

num.sort()
ans = []

# print("hh", ans)
for x in num:
  ans.append(x * N)
  N -= 1
# print(ans)
print(max(ans))


# 그리디는 브루트 포스 방법 중 하나 !! 너무 다 줄일 필요는 없다 !!