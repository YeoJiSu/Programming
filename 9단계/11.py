import sys
import math
def count_position(x1, y1, r1, x2, y2, r2):
    if (x1, y1) == (x2, y2) and r1 == r2: # 일치하면 무한대 
        return -1
    len = math.sqrt((x1-x2)**2+ (y1-y2)**2) # 점과 점사이의 거리
    if r1> r2:
        max = r1
        min = r2
    else:
        min = r1
        max = r2
        
    if len == r1+r2 or len + min == max: # 한점에서 만나는 경우
        return 1
    elif len > r1+r2 or len + min < max: # 안만나는 경우
        return 0
    else: # 두점에서 만나는 경우
        return 2
    
def main():
    T = int(sys.stdin.readline())
    for i in range(0,T):
        x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split(" "))
        print(count_position(x1, y1, r1, x2, y2, r2))
main()

