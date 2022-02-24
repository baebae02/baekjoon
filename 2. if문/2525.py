#2525
h, m = map(int, input().split())
time = int(input())

m = m + time
plus = int(m / 60)
h = h + plus
print(h % 24, m % 60)
