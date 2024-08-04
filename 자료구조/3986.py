N = int(input())

def checkgood(s):
  stack = []
  for i in s:
    if stack and stack[-1] == i:
      stack.pop()
    else:
      stack.append(i)
  return len(stack) == 0

cnt = 0

for _ in range(N):
  cnt += checkgood(input())

print(cnt)