N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]
for _ in range(M):
  i, j = map(int, input().split())
  desc = reversed(basket[i-1:j])
  basket[i-1:j] = desc

print(*basket)