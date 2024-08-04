S = list(input())
T = list(input())

while True:
  if len(S) == len(T):
    if S == T:
      print(1)
    else:
      print(0)
    break
  if T[-1] == 'A':
    T.pop()
  else:
    T.pop()
    T = T[::-1]
