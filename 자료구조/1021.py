from collections import deque
N, M = map(int, input().split())
targets = list(map(int, input().split()))

queue = deque([i for i in range(1, N+1)])
cnt=0

for i in range(M):
  target = targets[i]
  idx = queue.index(target)
  # print(target, idx)
  if idx < len(queue) - idx:
    while queue[0] != target:
      # print("queue", queue)
      queue.append(queue.popleft()) # 앞에꺼 빼서 뒤에 넣기
      cnt += 1
  else:
    while queue[0] != target:
      # print("queue2", queue)
      queue.appendleft(queue.pop()) # 뒤에꺼 빼서 앞에 넣기
      cnt += 1
  queue.popleft()
  
print(cnt)