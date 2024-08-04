S = list(map(int, list(input())))

cnt021 = 0
cnt120 = 0
for i in range(len(S)-1):
  if S[i] == 1 and S[i] != S[i+1]:
    cnt120 += 1
  if S[i] == 0 and S[i] != S[i+1]:
    cnt021 += 1

print(max(cnt021, cnt120))
