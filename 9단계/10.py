import sys
import math
num = int(sys.stdin.readline())
# 택시기하학 공식 해석해보니까 정사각형모양 마름모 그려짐 
print("{:.5f}".format(num**2*math.pi))
print("{:.5f}".format(num**2*2)) # 2곱한건 루트 2 제곱한거라서 