import sys
def main():
    while True:
        string = sys.stdin.readline()
        if string==".\n":
            break
        vps(list(string))

def vps(st):
    a = []
    for i in st:
        if i == "("or i=="[":
            a.append(i)
        elif i == ")":
            if len(a)!=0 and a[-1]=="(":
                a.pop()
            else:
                a.append(i)
                break
        elif i == "]":
            if len(a)!=0 and a[-1]=="[":
                a.pop()
            else:
                a.append(i)
                break
    if len(a)==0:
        print("yes")
    else:
        print("no")
                

main()