import sys

i = 0 
while True: 
    try:
        a, b = map(int, sys.stdin.readline().split())
        print("{}".format(a+b))
    except:
        break