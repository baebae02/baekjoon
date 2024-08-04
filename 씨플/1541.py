minuslist = (input().split("-"))

total = 0
for i in range(len(minuslist)):
  if i == 0:
    nums = map(int, minuslist[0].split("+"))
    total += sum(nums)
  else:
    nums = map(int, minuslist[i].split("+"))
    total -= sum(nums)
  
print(total)