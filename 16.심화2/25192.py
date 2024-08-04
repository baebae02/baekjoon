N=int(input())
cnt = 0
s = set()
for _ in range(N):
  cmd = input()
  if cmd == "ENTER":
    cnt += len(s)
    s = set()
  else:
    s.add(cmd)
print(cnt + len(s))