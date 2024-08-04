N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
S = list(map(int, input().split()))

# 이진 탐색
for i in S:
  start = 0
  end = N-1

  while start <= end:
    mid = (start + end) // 2
    # print(start, end, mid, i, "\n")
    if i < A[mid]: 
      end = mid-1
    elif A[mid] < i:
      start = mid+1
    else:
      start = mid
      end = mid
      break
    
  if start == mid and end == mid:
    print(1)
  else:
    print(0)




