li = []
s = set(li)
for i in range(0,10):
    n = int(input()) % 42
    s.add(n)
print(len(s))