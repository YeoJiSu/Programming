import sys
def main():
    N = int(sys.stdin.readline())
    for m in range(1,N):
        if m+num(m) == N :
            print(m)
            exit()
    print(0)

def num(m): # 각자리 숫자 합 구하기
    sum = 0
    n = m
    while n>0:
        sum+=n%10
        n=int(n/10)
    return sum

main()

