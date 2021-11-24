import sys
num = int(sys.stdin.readline())

i = 1
while True:
    if num >= 2+ 3*(i-2)*(i-1) and num <= 1+ 3*(i-1)*i:
        break
    i+=1
print(i)
# 이렇게 하면 시간초과 에러 발생함 
