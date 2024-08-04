from collections import deque
N, K = map(int, input().split())
ans = []
people = [i for i in range(1, N+1)]

# 1 2 4 5 6 7
index = K-1
while people:
  print(people, ans, index, K)
  ans.append(str(people.pop(index)))
  if not people:
    break
  index = (index-1+K) % len(people)

# 1 2 4 5 7

print("<", ", ".join(ans), ">", sep='')

# print sep 기억
# index는 i로 고정, 나머지 연산을 조정하기