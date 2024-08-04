n = input()
s = []
cnt = 0

for i in range(len(n)):
  if n[i] == '(':
    s.append('(')
  else:
    if n[i-1] == '(':
      s.pop()
      cnt += len(s)
    else:
      s.pop()
      cnt += 1
    

print(cnt)
  