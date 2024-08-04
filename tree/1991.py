N = int(input())
g = {}


# 전위 순위
def preorder(root):
  if root != '.':
    print(root, end='')
    preorder(g[root][0])
    preorder(g[root][1])


# 중위 순위
def inorder(root):
  if root != '.':
    inorder(g[root][0])
    print(root, end='')
    inorder(g[root][1])

# 후위 순위
def postorder(root):
  if root != '.':
    postorder(g[root][0])
    postorder(g[root][1])
    print(root, end='')

for i in range(N):
  node, left, right = input().split()
  g[node] = [left, right]



preorder('A')
print()
inorder('A')
print()
postorder('A')