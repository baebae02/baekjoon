from collections import deque

n = int(input())
num = []
for _ in range(n):
  a, b = map(int ,input().split())
  num.append([a,b])


prime_list = [False, False] + [True] * 9999
primes = []
for i in range(2, 10000):
  if prime_list[i]:
    if i >= 1000: primes.append(i)
    for j in range(2*i, 10000, i):
      prime_list[j] = False


def check_equal(a, b):
  a = list(str(a))
  b = list(str(b))
  cnt = 0
  for i in range(4):
    if a[i] == b[i]:
      cnt += 1
  return cnt == 3

# visited = []
#bfs
# visited[1373] = 1
def search(now, target, cnt):
  queue = deque()
  queue.append([now, cnt])
  while queue:
    now, cnt = queue.popleft()
    if now == target:
      print(cnt)
      return
    for prime in primes:
      # prime이랑 now랑 1자리 차이나는 지 확인
        if not visited[prime] and check_equal(now, prime):
          # print(prime, cnt + 1)
          # visited.append(prime)
          visited[prime] = 1
          queue.append([prime, cnt + 1])
        # queue.append(prime)
    # 1자리 차이나는 소수는 visited에 추가 
    # 1자리 늘어났는데 그 target이랑 같으면 return

# search(1373, 8017, 0)

# graph = [x][y][z][r]
for i in num:
  visited = [0] * 10000
  search(i[0], i[1], 0)
