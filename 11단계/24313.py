# 백준 24313번: 알고리즘 수업 - 점근적 표기 1
import sys
a, b = map(int, sys.stdin.readline().split(' '))
c = int(sys.stdin.readline()) # 양의 정수
n = int(sys.stdin.readline()) # 

"""
a*n + b <= c*n
b<=(c-a)*n

만약 c-a가 양수라면, b<=1이어야함.
만약 c-a가 0이면, b <= 0이어야함. 
그리고 c-a는 음수가 되면 안됨. 
"""

# 답
if (c-a>0) and (b<=(c-a)*n):
     print(1)
elif (c-a==0) and (b<=0):
     print(1)
else:
     print(0)

# 이렇게 줄여도 됨. 
if (c-a>=0) and (b<=(c-a)*n):
     print(1)
else:
     print(0)