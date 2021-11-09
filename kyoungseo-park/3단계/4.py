import sys

 
i_count = int(sys.stdin.readline())
a = 0

for i in range(1, i_count + 1):
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    
    print(a+b)
