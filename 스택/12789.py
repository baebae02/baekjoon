from collections import deque
N = int(input())
stds = deque(map(int, input().split()))
que = deque()
# print(stds)
cnt = 1

def cal():
  global cnt
  while len(stds) != 0:
    # print("==stds==", stds)
    # print("==que==", que)
    now = stds[0]
    if cnt == now:
      stds.popleft()
      cnt += 1
    elif que and que[0] == cnt:
      que.popleft()
      cnt += 1
    else:
      if que and que[0] < now:
        return "Sad"
      else:
        stds.popleft()
        que.appendleft(now)
  return "Nice"

print(cal())


# pop left를 먼저 해서 now를 선언하는 바람에 마지막 케이스가 while 문을 빠져나와서 틀림