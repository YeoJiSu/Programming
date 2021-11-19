import sys
num = sys.stdin.readline().split("\n")[0]
li =list(map(str,num.split(" ")))
count=len(li)
for i in li:
    if i=='':
        count-=1
print(count)