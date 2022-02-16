import sys
X, Y = map (int, sys.stdin.readline().split(' '))
if X==Y:
    print(-1)
    exit()
try:
    Z=int((Y*100)/X)
    a = ((Z+1)*X - 100*Y)/(99-Z)
    if a.is_integer():
        print(int(a))
    else:
        print(int(a)+1)
    
except:
    print(-1)