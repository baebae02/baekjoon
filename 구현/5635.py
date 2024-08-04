n = int(input())
bday = []
for _ in range(n):
  name, day, month, year = input().split()
  bday.append([year, month, day, name])

bday.sort(key=lambda x: (int(x[0]), int(x[1]), int(x[2])))
print(bday[-1][3])
print(bday[0][3])
