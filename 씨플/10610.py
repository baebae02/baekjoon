N = list(map(int, list(input())))

def check(N):
  if 0 not in N:
    print(-1)
    return -1
  if (sum(N) % 3) != 0:
    print(-1)
    return -1
  else:
    N.sort(reverse=True)
    print(*N, sep='')
    return 0
  
check(N)
