# from itertools import permutations
# N, M = map(int, input().split())

# per = list(permutations(range(1, N+1),M))

# for k in per:
#   print(*k, sep=' ')

# 백트레킹 써서 다시 풀어보기

N, M = map(int, input().split())
array = []

def backtracking():
  if len(array) == M:
    print(" ".join(map(str, array)))
    return
  for i in range(1, N+1):
    if i not in array:
      array.append(i)
      backtracking()
      array.pop()
  
backtracking()