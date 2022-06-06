import sys
T = int(sys.stdin.readline())
for i in range(T):
    count = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split(" "))
    n = int(sys.stdin.readline())
    for i in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split(" "))
        first = (cx-x1)**2 + (cy-y1)**2 <= r**2
        second = (cx-x2)**2 + (cy-y2)**2 <= r**2
        if (first or second):
            count+=1
            if (first and second): # 시작점과 도착점이 같은 원 안에 있는 경우, count하면 안됨
                count-=1
    print(count)