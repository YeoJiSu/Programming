# 11729번 재귀 - 하노이탑 이동순서
import sys
N = int(sys.stdin.readline())
arr = []
def hanoi(count, start, goal, sub):
    if count == 1:
        arr.append([start,goal])
        return
    hanoi(count-1, start, sub, goal)
    arr.append([start,goal])
    hanoi(count-1, sub, goal, start)
hanoi(N,1,3,2)
print(len(arr))
for i in arr:
    print(i[0],i[1])