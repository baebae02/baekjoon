E, S, M = map(int, input().split())
i = 1
E_val, S_val, M_val = 1, 1, 1
while True:
  if E_val == E and S_val == S and M_val == M:
    print(i)
    break
  i += 1; E_val += 1; S_val += 1; M_val += 1;
  if E_val >= 16: E_val -= 15
  if S_val >= 29: S_val -= 28
  if M_val >= 20: M_val -= 19

