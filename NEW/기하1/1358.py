import sys
W, H, X, Y, P = map(int, sys.stdin.readline().split(" "))
count = 0
def check(a,b):
    global count
    if (a>=X and a<=X+W) and (b>=Y and b<=Y+H):
        count+=1
    elif ((X-a)**2 + (Y+H/2 - b)**2 <= (H/2)**2 or (X+W-a)**2 + (Y+H/2 - b)**2<= (H/2)**2):
        count+=1
    
for i in range(P):
    a,b = map(int, sys.stdin.readline().split(" "))
    check(a,b)
print(count)

