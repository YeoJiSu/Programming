import sys
import math
def main():
    num = int(sys.stdin.readline())
    divide = list(map(int,sys.stdin.readline().split(" ")))
    sort = sorted(divide)
    print(sort[0]*sort[num-1])
main()
