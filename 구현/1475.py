import math
N = list(input())
n = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}

for i in N:
  if i == '9':
    n['6'] += 1
  else:
    n[i] += 1

n['6'] = math.ceil(n['6']/2)

print(max(n.values()))