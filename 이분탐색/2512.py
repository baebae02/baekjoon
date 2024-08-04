N = int(input())
moneys = list(map(int, input().split()))

M = int(input())
start, end = 1, max(moneys)
mid = 0

while start <= end:
  mid = (start + end) // 2
  total = 0
  for money in moneys:
    total += min(mid, money)
  if total <= M:
    start = mid + 1
  else:
    end = mid - 1

print(end)
