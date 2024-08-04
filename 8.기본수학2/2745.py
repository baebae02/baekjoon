N, B = input().split()
N = list(N)
N.reverse()
B = int(B)
sum = 0
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(N)):
  sum += B ** i * num_list.index(N[i])

print(sum)
