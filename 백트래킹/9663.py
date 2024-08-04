N = int(input())
chess = [0]*N
ans = 0

def valid(x):
  for i in range(x):
    if chess[i] == chess[x] or abs(chess[x]-chess[i]) == abs(x-i):
      return False
  return True

def backtracking(x):
  global ans
  if x == N:
    ans += 1
    return
  else:
    for i in range(N):
      chess[x] = i
      if valid(x):
        backtracking(x+1)


backtracking(0)
print(ans)