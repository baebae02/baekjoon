# from collections import deque
# q = deque()
# A, B = map(int, input().split())
# q.append((A, 1))

# while q:
#   now, count = q.popleft()
#   # print(B, A, count)
#   if now > B:
#     continue
#   if B == now:
#     print(count)
#     break
#   q.append((A*2, count + 1))
#   q.append((A * 10 + 1, count + 1))
# else:
#   print(-1)

# 이것도 마찬가지. 방법은 맞았으나 한번에 끝내면 안되고 모든 경우를 탐색해야 함. BFS로 함께 탐색.
# 162
# 81
# 8
# 4
# 2

# 42
# 21
# 2


# 40021
# 4002
# 2001
# 200
# 100




A, B = map(int, input().split())

def cal(A,B):
  count = 1
  while B != A:
    # print(B, A, count)
    temp = B
    if B % 10 == 1:
      B = B // 10
    elif B % 2 == 0:
      B = B // 2
    if temp == B:
      return -1
    count += 1
  return count

print(cal(A, B))