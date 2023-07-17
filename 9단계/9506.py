# 9506번 - 약수들의 합
import sys

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    
    _sum = 1
    _word = "1"
    for i in range(2,n//2+1):
        if n%i == 0:
            _sum+=i
            _word+=" + "+str(i)
    if _sum == n:
        print(str(n)+" = "+_word)
    else:
        print(str(n)+" is NOT perfect.")