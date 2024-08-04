import sys
input = sys.stdin.readline
N, M = map(int, input().split())
words = {}
for _ in range(N):
  word = input().rstrip()
  if len(word) < M:
    continue
  if word in words:
    words[word] += 1
  else:
    words[word] = 1

newList = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for k in newList:
  print(k[0])


# 틀린이유: 시간초과 날 땐 for문 제거 할 방법 떠올리기.
#       : list sorted 다중 우선순위 할 때 reverse는 - 붙여서 해결
# 잘한거: rstrip 떠올리기 & dict로 접근하기