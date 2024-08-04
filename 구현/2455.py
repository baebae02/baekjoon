people = 0
maximum = 0
for _ in range(4):
  off, on = map(int, input().split())
  people += on
  people -= off
  maximum = max(maximum, people)

print(maximum)