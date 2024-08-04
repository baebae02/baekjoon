#좋은 암호
K, L = map(int, input().split())
flag="GOOD"
for i in range(2, L):
    if(K%i == 0):
        flag="BAD"
        break

if flag == "BAD":
    print(flag, i)
else:
    print(flag)

