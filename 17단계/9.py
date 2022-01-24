import sys
import math
num = int(sys.stdin.readline())
for i in range(0,num):
    m, n =map(int, sys.stdin.readline().split())
    result = math.factorial(n)//(math.factorial(m)*math.factorial(n-m))
    print(result)