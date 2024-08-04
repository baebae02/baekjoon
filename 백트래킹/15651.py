N, M = map(int, input().split())
array = []

def backtracking():
  if len(array) == M:
    print(" ".join(map(str, array)))
    return
  for i in range(1, N+1):
    array.append(i)
    backtracking()
    array.pop()
  
backtracking()