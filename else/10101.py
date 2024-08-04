angle = []
for _ in range(3):
  angle.append(int(input()))

angle.sort()
if sum(angle) != 180:
  print("Error")
elif min(angle) == max(angle):
  print('Equilateral')
elif (angle[0] == angle[1] or angle[1] == angle[2]):
  print("Isosceles")
elif sum(angle) == 180:
  print("Scalene")