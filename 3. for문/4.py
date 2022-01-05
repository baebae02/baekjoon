import sys
n = int(sys.stdin.readline())

for i in range(0,n) :
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d + %d = %d" %(i+1, a,b,a+b))

# input() 보다 sys.stdin.readline()이 빠름. 특히 반복문에서 이걸 써야 시간이 절약 !! 5