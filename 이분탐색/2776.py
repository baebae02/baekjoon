import sys
input = sys.stdin.readline

T = int(input())

def binary_search(n, m, ns):
  start, end = 0, n - 1
  while start <= end:
    mid = (start + end) // 2
    # print(start, end, ns, mid)
    if ns[mid] == m:
      return True
    elif ns[mid] > m:
      end = mid - 1
    else:
      start = mid + 1
  return False


for _ in range(T):
  N = int(input())
  ns = list(map(int, input().split()))
  ns.sort()
  M = int(input())
  ms = list(map(int, input().split()))
  for m in ms:
    if binary_search(N, m, ns):
      print(1)
    else:
      print(0)
