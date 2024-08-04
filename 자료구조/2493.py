import sys
input = sys.stdin.readline

N = int(input())
tops = list(map(int, input().split()))
stack = []

for i in range(N):
  if not len(stack):
    stack.append([tops[i], i])
    print(0, end=' ')
  else:
    while stack:
      if stack[-1][0] < tops[i]:
        stack.pop()
        if not stack:
          print(0, end=' ')
      elif stack[-1][0] > tops[i]:
        print(stack[-1][1]+1, end=' ')
        break
      else:
        print(stack[-1][1]+1, end=' ')
        stack.pop()
        break
    stack.append([tops[i], i])



# dp = [[0,0]] * N
# ans = [0] * N
# dp[0] = [tops[0], 1]

# for i in range(1, N):
#   # print(dp)
#   # print(ans)
#   if dp[i-1][0] < tops[i]: 
#     dp[i][0] = tops[i]
#     dp[i][1] = i+1
#   else:
#     max_dp_index = dp[i-1][1]
#     # print(i, max_dp_index, "----")
#     dp[i] = dp[i-1]
#     for j in range(i-1, max_dp_index-2, -1):
#       # print(j, tops[j], tops[i], i)
#       if tops[j] >= tops[i]:
#         ans[i] = j+1
#         break


    
# print(ans)



# 0 0 0 0 0
# (6,1) (9,1) 0 0 0
# 6 9 5 7 4