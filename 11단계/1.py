import sys
def main():
    N,M = map(int, sys.stdin.readline().split(" "))
    num = list(map(int, sys.stdin.readline().split(" ")))
    dif = M
    for i in range(0,N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                sum = num[i]+num[j]+num[k]
                if sum == M:
                    print(sum)
                    exit()
                if 0< M-sum <= dif:
                    dif = M-sum
                    result = sum
    print(result)
    
main()

