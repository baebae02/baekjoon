M, N = map(int, input().split())
chest = [True] * (N+1)
chest[0] = False
chest[1] = False

for i in range(2, int(N**0.5)+1):
  j = 2
  while i*j <= N:
    chest[i*j] = False
    j += 1

for k in range(M, N+1):
  if chest[k] == True:
    print(k)