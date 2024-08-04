T = int(input())
A = 5 * 60
B = 60
C = 10

if T%C == 0:
  print(T//A, T%A//B, T%B//C)
else:
  print(-1)