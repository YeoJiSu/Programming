import sys
def main():
    num = int(sys.stdin.readline())
    for i in range(0,num):
        string = sys.stdin.readline()
        vps(list(string))

def vps(st):
    a = []
    for i in st:
        if i == "(":
            a.append(i)
        elif i == ")":
            if len(a)!=0 and a[-1]=="(":
                a.pop()
            else:
                a.append(i)
                break
    if len(a)==0:
        print("YES")
    else:
        print("NO")
                

main()