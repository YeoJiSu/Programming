import sys
str = sys.stdin.readline()
str=str.split("\n")[0].upper()
alpha=[]
count=[]
for i in str:
    if i not in alpha:
        alpha.append(i)
        count.append(0)
    if i in alpha:
        new = count[alpha.index(i)]+1
        count[alpha.index(i)]=new
sor = sorted(count)
if len(sor)==1: # 이거 추가 안했더니 런타임 에러 발생했었음
    print(alpha[0])
elif sor[-1]==sor[-2]: # 이거 -2 를 참조해서 그런것 같음 
    print("?")
else:
    print(alpha[count.index(max(count))])
