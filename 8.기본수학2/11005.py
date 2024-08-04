N, B = map(int, input().split())
ans = []
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while True:
  x = N % B
  x = num_list[x]
  ans.append(x)
  N = N // B
  if N == 0:
    break

ans.reverse()
print(''.join(ans))