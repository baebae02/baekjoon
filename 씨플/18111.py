import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

mc = []
for _ in range(N):
  mc.append(list(map(int, input().split())))

glevel = min(min(mc))
ans = int(1e9)

for i in range(glevel, 257):
  use_block = 0
  take_block = 0
  for x in range(N):
    for y in range(M):
      if mc[x][y] > i:
        take_block += mc[x][y] - i
      else:
        use_block += i - mc[x][y]
    
  if use_block > take_block + B:
    continue
    
  time = take_block * 2 + use_block
  if time <= ans: # 이 등호로 조건 만족
    ans = time
    glevel = i

print(ans, glevel)

# 기계적으로 생각하는 게 필요. 컴퓨터는 어디가 적정지점인지 모른다. 그래서 브루트 포스가 필요한 것.
# use_block과 take_block 두 식만 사용해서 시간이 얼마나 필요한지 계산하는 센스