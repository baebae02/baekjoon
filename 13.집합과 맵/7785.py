from sys import stdin
from collections import deque

n = int(input())
work = []
for _ in range(n):
  name, status = stdin.readline().split()
  if status == "enter":
    work.append(name)
  if status == "leave":
    work.remove(name)

work.sort(reverse=True)
print(*work, sep="\n")