from collections import Counter
an, bn = map(int,input().split())
A = Counter(list(map(int, input().split())))
B = Counter(list(map(int, input().split())))
cntA = len(A)
for i in A:
    if B[i] == 1:
        del B[i]
        cntA -= 1
cnt = len(B) + cntA
print(cnt)
