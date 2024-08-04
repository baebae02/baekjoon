from collections import Counter
N = int(input())
sang = list(map(int, input().split()))
c = Counter(sang)

M = int(input())
card = list(map(int, input().split()))
for i in card:
    print(c[i], end= ' ')
