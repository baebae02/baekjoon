A, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

def merge_sort(num_list, start, end):
  # start < end 일 때 까지 반으로 쪼개서 정렬하고 마지막에 합치고!
  if start < end:
    mid = (start + end) // 2
    merge_sort(num_list, start, mid)
    merge_sort(num_list, mid+1, end)
    merge(num_list, start, mid, end)
  
# num_list[start:mid]랑 num_list[mid+1:end]를 비교하며 병합한다. 
def merge(num_list, start, mid, end):
  global cnt, res
  i = start
  j = mid + 1
  tmp = []

  while i <= mid and j <= end:
    if num_list[i] <= num_list[j]:
      tmp.append(num_list[i]) # 전자가 더 클 경우
      i += 1
    else:
      tmp.append(num_list[j]) # 후자가 더 클 경우
      j += 1

  # 전자 리스트에 남은 거 다 넣기
  while i <= mid:
    tmp.append(num_list[i])
    i+=1
  
  # 후자 리스트에 남은 거 다 넣기
  while j <= end:
    tmp.append(num_list[j])
    j+=1

  # 전체 리스트를 A에 다시 복사하기
  i = start
  t = 0
  while i <= end:
    num_list[i] = tmp[t]
    cnt += 1
    # print(num_list, tmp)
    if cnt == K: # K번 다 저장해버리면
      res = num_list[i]
      break
    t += 1
    i += 1

res = -1
merge_sort(arr, 0, A-1)
print(res)
