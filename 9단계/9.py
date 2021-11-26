import sys
while True:
    my=list(map(int, sys.stdin.readline().split(" ")))
    if sum(my)==0:
        exit()
    my=sorted(my)
    if (my[0]**2+my[1]**2 == my[2]**2):
        print("right")
    else:
        print("wrong")
    