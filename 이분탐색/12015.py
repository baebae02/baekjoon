N = int(input())
A = list(map(int, input().split()))

def find_index(num):
  start, end = 0, len(res) - 1
  mid = 0
  while start <= end:
    mid = (start + end) // 2
    print(start, end)
    if res[mid] >= num:
      end = mid - 1
      return mid
    else:
      start = mid + 1
  return start


res = [A[0]]
for num in A:
  if num > res[-1]:
    res.append(num)
  else:
    index = find_index(num)
    res[index] = num
  

print(len(res))