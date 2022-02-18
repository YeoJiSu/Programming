import re
import sys
def min_value():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split(" ")))
    B = list(map(int, sys.stdin.readline().split(" ")))
    A.sort()
    B.sort(reverse=True)
    sum_ = 0
    for i in range(N):
        sum_+=A[i]*B[i]
    print(sum_)
if __name__ == "__main__":
    min_value()