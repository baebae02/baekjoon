A, B = map(int, input().split())
C, D = map(int, input().split())

E = A*D + C*B
F = B*D

G = max(E, F)
H = min(E, F)

while H != 0:
  G = G % H
  G, H = H, G
print(E // G, F // G)



