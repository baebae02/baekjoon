import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dna = []
sample = ['A', 'C', 'G', 'T']
for _ in range(N):
  dna.append(input())

dna.sort()
# print(dna)

h_d = [[0, 0, 0, 0] for _ in range(M)] # A C G T

for i in range(N):
  target = dna[i]
  for j in range(M):
    if target[j] == sample[0]:
      h_d[j][0] += 1
    elif target[j] == sample[1]:
      h_d[j][1] += 1
    elif target[j] == sample[2]:
      h_d[j][2] += 1
    elif target[j] == sample[3]:
      h_d[j][3] += 1

# print(h_d)
cnt = 0
for i in range(M):
  target = h_d[i]
  max_char = target.index(max(target))
  # print("max", max(target))
  cnt += N - max(target)
  print(sample[max_char], end='')

print()
print(cnt)
