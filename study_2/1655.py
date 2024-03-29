import sys, heapq

from torch import max_pool1d

N = int(sys.stdin.readline())
max_heap, min_heap = [], []

def insertNum(num):
	if len(max_heap) == len(min_heap):
		heapq.heappush(max_heap, (-num, num))
	else:
		heapq.heappush(min_heap, num)
	if min_heap:
		if max_heap[0][1] > min_heap[0]:
			temp1, temp2 = heapq.heappop(max_heap)[1], heapq.heappop(min_heap)
			heapq.heappush(max_heap, (-temp2, temp2))
			heapq.heappush(min_heap, temp1)
	
for _ in range(N):
	num = int(sys.stdin.readline())
	insertNum(num)
	print(max_heap[0][1])