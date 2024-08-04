s = list(input())

ans = []
sliding = 0


def check_status():
  if sliding % 4 == 0:
    return "A"*(sliding)
  elif sliding > 4 and sliding % 2 == 0:
    return "A" * ((sliding//4) * 4) + "B" * (sliding% 4)
  elif sliding % 2 == 0:
    return "B"*sliding
  else:
    return -1
  
for k in s:
  if k == '.':
    if sliding > 0:
      result = check_status()
      if result == -1:
        print(-1)
        exit()
      else:
        ans.append(result)
      sliding = 0
    ans.append(".")
  else:
    sliding += 1

if sliding > 0:
  result = check_status()
  if result == -1:
        print(-1)
        exit()
  else:
    ans.append(result)

print("".join(ans))