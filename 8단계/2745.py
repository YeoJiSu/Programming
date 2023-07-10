# 백준 2745번 - 진법 변환
import sys

N, B = sys.stdin.readline().split('\n')[0].split(' ')
B = int(B)

_sum = 0
for i in range(len(N)-1,-1,-1):
    _mul = 1
    try:
        # 0~9 이면 숫자로 변환
        _mul = int(N[i])
    except:
        # A~Z 이면 10~35로 변환 -> 이때 아스키코드 활용
        _mul = ord(N[i])-55
    _sum+= _mul*(B**(len(N)-1-i))

print(_sum)