import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
  N = int(input())
  people = []
  count = 1
  for i in range(N):
    A, B = map(int, input().split())
    people.append((A,B))
  people.sort()
  min_B = people[0][1]
  # print(people, min_A, min_B)
  for p in people:
    # print(p[0], p[1])
    if p[1] >= min_B: #p[0] >= min_A 생략 가능 왜냐하면 정렬했으니까!
      continue
    else:
      min_B = p[1]
      count += 1
  print(count)
