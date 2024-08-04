N = int(input())
st = list()
for _ in range(N):
  st.append(list(input().split()))
# 국어 영어 수학
st.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# print(st)

for s in st:
  print(s[0])