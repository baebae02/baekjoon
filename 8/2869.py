#달팽이는 올라가고 싶다
import math
A, B, V = map(int, input().split())
day = math.ceil((V-A)/ (A-B))

print(day)