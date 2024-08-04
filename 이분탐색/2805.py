import sys
input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

if N == 1:
  print(trees[0]-M)
  exit()

if trees[1] - trees[0] >= M:
  print(trees[0]-M)
  exit()
  
start, end = 1, trees[0]
while start <= end:
  cutting_trees = 0
  mid = (start + end) // 2 # mid = 16 20
  for tree in trees:
    if tree > mid:
      cutting_trees += tree - mid
    else:
      break
  if cutting_trees >= M:
    start = mid + 1
  else:
    end = mid - 1

print(end)
