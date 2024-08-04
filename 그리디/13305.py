N = int(input())
edge = list(map(int, input().split()))
node = list(map(int, input().split()))
money = edge[0] * node[0]
min_cost = node[0]

for i in range(1, N-1):
  # print(i)
  # print("money", money, "min", min_cost)
  if node[i] < min_cost:
    min_cost = node[i]
  money += min_cost * edge[i]

print(money)

# 굳이 뒤에서 접근 할 필요 없음. min/max 업데이트 하면서 하나씩 계산하기