#ACM 호텔
import math
T = int(input())
for i in range(0,T) :
    H, W, N = map(int,input().split())
    if(N%H == 0):
        floor = H
    else: 
        floor = N%H
    
    unit = math.ceil(N/H)
    if(unit < 10):
        print(floor, "0", unit, sep='')
    else:
        print(floor, unit, sep='')