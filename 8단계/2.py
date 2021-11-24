import sys
num = int(sys.stdin.readline())

if num==1:
    print(1)
else:
    i = 1
    while True:
        if num >= 2+ 3*(i-2)*(i-1):
            if num <= 1+ 3*(i-1)*i:
                break
        i+=1
    print(i)
# 이렇게 하면 시간초과 에러 발생함 -> 원인이 1을 넣었을 때 무한 루프 돌아서였음 
