from collections import deque
S, P = map(int, input().split())
DNA = input()
A, C, G, T = map(int, input().split())

# 첫 슬라이딩 윈도우에서 ACGT 개수 새고 시작 !
left, right = 0, P-1
dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
arr = deque(DNA[left:right])
for i in arr:
  dic[i] += 1
count = 0

while right < S:
  # 구간 완성 
  dic[DNA[right]] += 1

  # 조건 비교
  if dic['A'] >= A and dic['C'] >= C and dic['G'] >= G and dic['T'] >= T:
    count += 1
  
  # 한 칸 밀기
  dic[DNA[left]] -= 1
  left += 1
  right += 1

print(count)

