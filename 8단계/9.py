import sys
import math
# 반복할 횟수
def count(n,m):
    N = m-n
    find = math.floor(math.sqrt(N))
    if (math.sqrt(N)==find):
        return find*2-1
    else:
        if (find*find+1) <= N <= (find*find + find):
            return find*2
        elif (find*find+find+1) <= N <= (find*find + 2*find):
            return find*2+1
    
def main():
    repeat = int(sys.stdin.readline())
    for i in range(0,repeat):
        n, m = map(int, sys.stdin.readline().split(" "))
        print(count(n,m))
main()

# 해결한 방법 ....
# 1. 제곱수 이면 
#       루트N * 2 -1 리턴
# 2. 제곱수 아니면  a 
#       a = math.floor(루트 N)
#       만약 a제곱+1   ~ a제곱+a   사이면 a*2 리턴
#       만약 a제곱+a+1 ~ a제곱+2a  사이면 a*2+1 리턴