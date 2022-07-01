# [a,b] 의 연속 XOR 값은 "[1,A-1]의 연속 XOR" ^ "[1,B]의 연속 XOR" 한 값과 같다 !
import sys
a,b = map(int, sys.stdin.readline().split(' '))
# [1,N]의 연속 XOR 한 값을 return 하는 함수
def xor(n):
    # 직접 해보면 아래와 같은 규칙이 찾아진다
    if n%4==0:
        return n
    if n%4==1:
        return n^(n-1)
    if n%4==2:
        return n^(n-1)^(n-2)
    if n%4==3:
        return 0
print(xor(b)^xor(a-1))