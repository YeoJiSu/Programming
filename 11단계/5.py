import sys

def main():
    N  = int(sys.stdin.readline())
    count = 0
    N_num = 666
    index = 0
    i = 0
    while True:
        if (count==N):
            break
        if "666" in (str(N_num)):
            count+=1
        N_num+=1   
        index+=1
    print(N_num-1)
main()
# 근데 더 쉬운 방법은 없나?