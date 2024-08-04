a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
print(1 if c*n0 >= a1*n0+a0 and c >= a1 else 0)
