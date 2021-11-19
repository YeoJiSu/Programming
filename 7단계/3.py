import sys
value = sys.stdin.readline().split("\n")[0]
alpha= [-1]*26
for i in value:
    index = ord(i)-97
    if alpha[index]==-1:
        alpha[index] = value.index(i)
for j in range(0,len(alpha)):
    str=" "
    if j==len(alpha)-1:
        str=""
    print(alpha[j], end=str)
    