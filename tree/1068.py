N = int(input())
nodes = list(map(int, input().split()))
del_node = int(input())

# for i in range(N):
#   print(nodes, i, nodes[i], del_node)
#   parent_node = nodes[i]
#   if i == del_node:
#     nodes[i] = -10
#   elif nodes[parent_node] == -10:
#     nodes[i] = -10

def dfs(del_node):
  nodes[del_node] = -10
  for i in range(N):
    if nodes[i] == del_node: # 누군가의 부모노드가 삭제된 노드라면
      dfs(i)

dfs(del_node)
cnt = 0
for j in range(N):
  if nodes[j] != -10 and j not in nodes:
    cnt+=1

print(cnt)