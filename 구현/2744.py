s = list(input())
for l in s:
  if ord(l) >= 97:
    print(chr(ord(l)-32), end='')
  else:
    print(chr(ord(l)+32), end='')