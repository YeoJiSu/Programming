import sys
num = int(sys.stdin.readline())

try:
    for i in range(0,num):
        line =sys.stdin.readline()
        a,str = int(line.split()[0]), line.split()[1]
        sum=""
        for i in str:
            sum+=i*a
        print(sum)
except:
    exit()

    