from collections import deque
def check(st):
  while True:
    if len(st) <= 1:
      return "yes"
    if st.pop() != st.popleft():
      return "no"
while True:
  s = input()
  if s == '0':
    break
  st = deque(map(int, list(s)))
  print(check(st))