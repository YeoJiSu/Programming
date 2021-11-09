import sys

i_number = int(sys.stdin.readline())

for i in range(1, i_number + 1):
    a, b = input().split()
    a = int(a)
    b = int(b)

    print("Case #{}: {}".format(i, a+b))
