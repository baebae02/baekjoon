N, K = map(int, input().split())
from collections import deque
# people = [i for i in range(1, N+1)]
ans = []

# while len(people) != 0:
#   if len(people) <= K:
#     K = K % len(people)
#   ans.append(people[K-1])
#   people.remove(people[K-1])
#   people = people[K-1:] + people[:K-1]

# 왜 틀렸는 지 모르겠음.

people = deque([i for i in range(1, N+1)])
while len(people) != 0:
  for _ in range(K-1):
    people.append(people.popleft())
  ans.append(people.popleft())

res = map(str, ans)
print("<", ", ".join(res), ">", sep="")