L, C =  map(int, input().split())
codes = list(input().split())
vowel = ['a', 'e', 'i', 'o', 'u']
vowel_cur = []

codes.sort()
ans_codes = []
# print(codes)
def backtracking(N, k):
  global ans_codes
  if N == L:
    cnt = 0
    for a in ans_codes:
      if a in vowel:
        cnt += 1
    if cnt >= L - 1 or cnt == 0:
      return 0
    print(*ans_codes, sep='')
    return 0
  for i in range(k, len(codes)): # len(codes) 대신 C 사용 가능
    temp = codes[i]
    # if temp in ans_codes: # 이거 없어도 됌. i+1이라 !
    #   continue
    ans_codes.append(temp)
    backtracking(N+1, i+1)
    del ans_codes[-1] # del [-1] 말고 pop 사용 가능
  
backtracking(0, 0)