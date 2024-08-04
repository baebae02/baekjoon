import sys
input = sys.stdin.readline
N, K = map(int, (input().split()))

A = list(map(int, input().split()))

def merge_sort(num_list):
  if len(num_list) <= 1:
    return num_list
  mid = len(num_list) // 2
  L = merge_sort(num_list[:mid])
  R = merge_sort(num_list[mid:])

  i, j, k = 0, 0, 0
  while i < len(L) and j < len(R):
    if L[i] <= R[j]:
      num_list[k] = L[i]
      i += 1
    else:
      num_list[k] = R[j]
      j += 1
    k += 1
  
  if i == len(L):
    while j < len(R):
        num_list[k] = R[j]
        j += 1
        k += 1
  elif j == len(R):
      while i < len(L):
          num_list[k] = L[i]
          i += 1
          k += 1
  return num_list


merge_sort(A)
# print(A)
print(A[K-1])
           


def merge_sort(arr):
  if len(arr) <= 1:
      return arr

  mid = len(arr) // 2
  L = merge_sort(arr[:mid])
  R = merge_sort(arr[mid:])
   
  i, j, k = 0
  while i < len(L) and j < len(R):
    if L[i] < R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1

  if i == len(L):
    while j <= len(R):
      arr[k] = R[j]
      j += 1
      k += 1
  elif j == len(R):
     while i <= len(L):
        arr[k] = L[i]
        i += 1
        k += 1
  return arr