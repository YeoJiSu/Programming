# 백준 2485번: 가로수
import sys
def gcd(a,b):
    if b>a:
        a,b = b,a
    if b==0:
        return a
    if a%b==0:
        return b
    else:
        return gcd(b, a%b)

n = int(sys.stdin.readline())
_list = [int(sys.stdin.readline())]
_gap = []
_gcd = 1
for i in range(1,n):
    before = _list[-1]
    after = int(sys.stdin.readline())
    _list.append(after)
    _gap.append(after-before)
    if i==2:
        _gcd = gcd(_gap[i-2],_gap[i-1])
    if i>=3:
        _gcd = gcd(_gap[i-1],_gcd)

_sum = 0
for i in _gap:
    _sum += i//_gcd -1
print(_sum)

"""  
첫번째) 2,4,6 -> 최대공약수: 2
1,2,3 -> 0,1,2 => 3

두번째) 4,6,6 -> 최대공약수: 2
2,3,3 -> 1,2,2 => 5
"""  