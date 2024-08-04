N = int(input())
s = set()
s.add("ChongChong")
for _ in range(N):
  a, b = input().split()
  if a in s or b in s:
    s.add(a)
    s.add(b)

print(len(s))