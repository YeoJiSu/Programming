import sys
def max_30():
    num = list(map(int,sys.stdin.readline().split("\n")[0]))
    num.sort(reverse=True)
    if sum(num)%3!=0 or num[-1]!=0:
        print(-1)
        exit()
    print(*num,sep="")
    
if __name__ == "__main__":
    max_30()