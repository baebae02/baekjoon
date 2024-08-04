from collections import deque
N, M, R = map(int, input().split())
A = []
answer = [[0] * M for _ in range(N)]
deq = deque()
loops = min(N, M) // 2
for _ in range(N):
  A.append(list(input().split()))

# 루프 돌리기 
for i in range(loops):
  deq.clear()
  deq.extend(A[i][i:M-i]) # 위
  deq.extend(row[M-i-1] for row in A[i+1:N-i-1]) # 오른쪽
  deq.extend(A[N-i-1][i:M-i][::-1]) # 아래쪽
  deq.extend(row[i] for row in A[i+1:N-i-1][::-1]) # 왼쪽

  deq.rotate(-R) # 덱 회전

  for j in range(i, M-i):
    answer[i][j] = deq.popleft()
  for j in range(i+1, N-i-1):
    answer[j][M-i-1] = deq.popleft()
  for j in range(M-1-i, i-1, -1):
    answer[N-i-1][j] = deq.popleft()
  for j in range(N-i-2, i, -1):
    answer[j][i] = deq.popleft()

# print(answer)
for line in answer:
    print(" ".join(line))

# 껍질 나눠서 돌리는 건 생각했으나 loop = min(N, M) // 2로 구해서 for 문 돌릴 생각은 못함
# index 처리가 정말 어려운 것 같음
# deque.extend에 대해 배움