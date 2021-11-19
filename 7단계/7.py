import sys
a,b = map(str,sys.stdin.readline().split())
a=''.join(reversed(a))
b=''.join(reversed(b))
try:
    if int(a)>int(b):
        print(a)
    else:
        print(b)
except:
    exit()

