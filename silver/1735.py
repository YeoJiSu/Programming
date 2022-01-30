import sys
def gcd(b,d):
    if d==0:
        return b
    return gcd(d,b%d)
def add():
    a,b =map(int,sys.stdin.readline().split())
    c,d = map(int,sys.stdin.readline().split())
    lcm = b*d // gcd(b,d)
    num = a*lcm//b + c*lcm//d
    divide = gcd(num, lcm)
    print(num//divide, lcm//divide)
if __name__ == "__main__":
    add()