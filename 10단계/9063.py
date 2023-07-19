# 백준 9063번 - 대지
import sys
N = int(sys.stdin.readline())

x_min = 10000
y_min = 10000
x_max = -10000
y_max = -10000
for i in range(N):
    A, B = map(int, sys.stdin.readline().split(' '))
    if x_min > A:
        x_min = A
    if x_max < A:
        x_max = A
    if y_min > B:
        y_min = B
    if y_max < B:
        y_max = B
print(abs(x_min-x_max)*abs(y_min-y_max))