from collections import Counter
N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))

li.sort()
mean = round(sum(li)/N)
medium = li[int((N-1)/2)]
counts = Counter(li).most_common()
range = li[-1] - li[0]
print(mean)
print(medium)

if len(counts) > 1:
    if counts[0][1] == counts[1][1]:
        print(counts[1][0])
    else:
        print(counts[0][0])
else:
    print(counts[0][0])
print(range)
