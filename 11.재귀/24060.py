N, K = map(int, input().split())
arr = list(map(int, input().split()))

temp = [0] * (N+1)
ans = []
def merge_sort(A, p, r):
  global ans
  if p < r:
    q = (p + r) // 2
    merge_sort(A, p, q)
    merge_sort(A, q+1, r)
    merge(A, p, q, r)


def merge(A, p, q, r):
  i = p
  j = q + 1
  t = 1
  while i <= q and j <= r:
    if A[i] <= A[j]:
      temp[t] = A[i]
      i+=1
      t+=1
    else:
      temp[t] = A[j]
      t+=1
      j+=1
  while i <= q:
    temp[t] = A[i]
    t+=1
    i+=1
  while j <= r:
    temp[t] = A[j]
    j+=1
    t+=1
  i = p 
  t = 1
  while i <= r:
    A[i] = temp[t]
    ans.append(A[i])
    i+=1
    t+=1

merge_sort(arr, 0, N-1)
print(ans)

if len(ans) < K:
  print(-1)
else:
  print(ans[K-1])