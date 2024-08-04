a = list(input())
b = list(input())
c = list(input())
d = list(input())
e = list(input())

while a or b or c or d or e:
  if a:
    print(a.pop(0), end='')
  if b:
    print(b.pop(0), end='')
  if c:
    print(c.pop(0), end='')
  if d:
    print(d.pop(0), end='')
  if e:
    print(e.pop(0), end='')