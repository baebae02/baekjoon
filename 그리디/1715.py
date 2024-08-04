import heapq
n = int(input())
num = []
for _ in range(n):
  heapq.heappush(num, int(input()))
  # num.append(int(input()))

if len(num) == 1:
  print(0)

else:
  answer = 0
  while len(num) > 1:
    temp_1 = heapq.heappop(num)
    temp_2 = heapq.heappop(num)
    answer += temp_1 + temp_2
    heapq.heappush(num, temp_1 + temp_2)

# 개념은 맞았으나 우선순위 큐를 사용할 생각은 못함.
  print(answer)