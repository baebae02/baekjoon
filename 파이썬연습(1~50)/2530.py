A, B, C = map(int, input().split())
D = int(input())

total = C + B*60 + A*60*60+D

A = (total // 3600) % 24
B = (total % 3600) // 60
C = (total % 60)

print(A, B, C)
