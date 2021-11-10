import sys

while True: 
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    if a+b == 0:
        break
    print("{}".format(a+b))