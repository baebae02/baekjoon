L, P, V = 1, 1, 1
cnt = 1
while L !=0 and P != 0 and V != 0:
  L, P, V = map(int, input().split())
  if L == 0 and P == 0 and V == 0:
    break
  if V % P <= L:
    print("Case {}: {}".format(cnt, V // P * L + V % P))
  else:
    print("Case {}: {}".format(cnt, V // P * L + L))
  cnt += 1