import sys
num = int(sys.stdin.readline())


i = 1
while True:
    if num>= 1+(i-1)*i/2:
        if num<=i*(i+1)/2:
            break
    i+=1
    
sum1 = i+1 # 분모와 분자의 합 sum1
sub = int(num-(1+(i-1)*i/2) +1) # 분자를 결정할 수 
#  i 가 짝수면 1부터 시작함 

if i%2==0:
    print("{0}/{1}".format(sub, sum1-sub))
else:
    print("{0}/{1}".format(sum1-sub,sub))
