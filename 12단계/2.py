import heapq
import sys
num = int(sys.stdin.readline())
heap = []
for i in range(num):
    heapq.heappush(heap,int(sys.stdin.readline()))
for j in range(num):
    print(heapq.heappop(heap))
