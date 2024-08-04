import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))

minimum = 1e9
maximum = -1e9

def backtracking(n, total, plus, minus, multi, divi):
  global minimum, maximum
  if n == N:
    minimum = min(total, minimum)
    maximum = max(total, maximum)
    return
  if plus:
    backtracking(n+1, total + A[n], plus - 1, minus, multi, divi)
  if minus:
    backtracking(n+1, total - A[n], plus, minus-1, multi, divi)
  if multi:
    backtracking(n+1, total * A[n], plus, minus, multi - 1, divi)
  if divi:
    backtracking(n+1, int(total / A[n]), plus, minus, multi, divi - 1)

backtracking(1, A[0], op[0], op[1], op[2], op[3])

print(maximum)
print(minimum)