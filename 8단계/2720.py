# 2720번 - 세탁소 사장 동혁
import sys
T = int(sys.stdin.readline())
quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01

for i in range(T):
    m = float(sys.stdin.readline())
    m = round(m / 100,2)
    a = int(m / quarter)
    m = round(m - a*quarter,2)
    b = int(m / dime)
    m = round(m - b*dime,2)
    c = int(m / nickel)
    m = round(m - c*nickel,2)
    d = int(m / penny)
    print(a,b,c,d)