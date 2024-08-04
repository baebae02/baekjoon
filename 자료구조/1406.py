from collections import deque
import sys
input = sys.stdin.readline

# s = input()
# M = int(input())
# s = s + "#" # 커서 위치

# for _ in range(M):
#   cmd = input().split()
#   cursor = s.index("#")
#   if cmd[0] == 'P':
#     left = s[:cursor]
#     right = s[cursor:]
#     s = left + cmd[1] + right # 커서 왼쪽에 문자 추가
  
#   elif cmd[0] == 'L' and cursor > 0:
#     left = s[:cursor-1]
#     mid = s[cursor-1]
#     right = s[cursor+1:]
#     s = left + "#" + mid + right # 커서를 왼쪽으로 이동
#   elif cmd[0] == 'D' and cursor < len(s)-1:
#     left = s[:cursor]
#     mid = s[cursor+1]
#     right = s[cursor+2:]
#     s = left + mid + "#" + right # 커서를 오른쪽으로 이동
#   elif cmd[0] == 'B' and cursor > 0:
#     left = s[:cursor-1]
#     right = s[cursor:]
#     s = left + right # 커서 왼쪽 문자 삭제

# cursor = s.index("#")
# s = s[:cursor] + s[cursor+1:]
# print(s)






L = deque(input())
R = deque()
L.pop()
for _ in range(int(input())):
  cmd = input().split()
  print(L, R, cmd)
  if cmd[0] == 'L' and L: R.appendleft(L.pop())
  elif cmd[0] == 'D' and R: L.append(R.popleft())
  elif cmd[0] == 'B' and L: L.pop()
  elif cmd[0] == 'P': L.append(cmd[1])


print(''.join(L) + ''.join(R))