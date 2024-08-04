import heapq
import sys
input = sys.stdin.readline
N = int(input())
h = []
for _ in range(N):
  h.append(list(map(int, input().split())))

h.sort(key=lambda x: (x[0]))
room = []
heapq.heappush(room, h[0][1])

for i in range(1, N):
  if room[0] <= h[i][0]:
    heapq.heappop(room)
  heapq.heappush(room, h[i][1])

print(room)

print(len(room))