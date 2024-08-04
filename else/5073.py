length= list(map(int, input().split()))
while sum(length) != 0:
  length.sort()
  if length[0] == length[1] and length[1] == length[2]:
    print("Equilateral")
  elif length[2] >= length[0] + length[1]:
    print("Invalid")
  elif length[0] == length[1] or length[1] == length[2]:
    print("Isosceles")
  elif length[0] != length[1] and length[1] != length[2]:
    print("Scalene")
  else:
    print("Invalid")
  length= list(map(int, input().split()))