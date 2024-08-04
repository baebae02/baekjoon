N = int(input())
A = list(map(int, input().split()))

# A =  A
# 10 -4 3 1 5 6 -35 12 21 -1

# 33

# 10 6 9 10 15 21 0 12 33 33

# 2 1 -4 3 4 -4 6 5 -5 1
# 2 3 0 3 7 3 9 14 9 10
# print(A)

for i in range(1, N):
  # print(A,i)
  A[i] = max(A[i], A[i-1]+ A[i])

print(max(A))


# -1 -2 -3 -4 -5
# -1 -3