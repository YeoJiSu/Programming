import sys

# 문제에 나와있는 내용 그대로 코드로 옮겼을 때  
def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if a < b and b < c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        return  w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

def getAnswer():
    while True:
        a,b,c = map(int, sys.stdin.readline().split(' '))
        if a==-1 and b==-1 and c==-1:
            break
        result = w(a,b,c)
        print("w({0}, {1}, {2}) = {3}".format(a,b,c,result))

# 동적계획법으로 해결하는 풀이법
w = [[[1 for k in range(20)] for j in range(20)]for i in range(20)] # 3차원 배열의 모든 원소를 1로 초기화 하기

for i in range(0,20):
    for j in range(0,20):
        for k in range(0,20):
            first = 1
            second = 1
            third = 1
            fourth = 1
            if i<j and j<k:
                if k!=0: 
                    first = w[i][j][k-1]
                    if j!=0: # k, j 둘다 0이 아닐 때
                        second = w[i][j-1][k-1]
                if j!=0:
                    third = w[i][j-1][k]
                w[i][j][k] = first + second - third
            else:
                if i!=0:
                    first = w[i-1][j][k]
                    if j!=0:
                        second = w[i-1][j-1][k]
                        if k!=0:
                            fourth = w[i-1][j-1][k-1]
                    if k!=0:
                        third = w[i-1][j][k-1]
                w[i][j][k] = first + second + third - fourth

# 정답 출력하기              
def getAnswerDP():
    while True:
        a,b,c = map(int, sys.stdin.readline().split(' '))
        if a==-1 and b==-1 and c==-1:
            break
        if a <= 0 or b <= 0 or c <= 0:
            result = 1
        elif a > 20 or b > 20 or c > 20:
            result = w[19][19][19]
        else:
            result = w[a-1][b-1][c-1]
        print("w({0}, {1}, {2}) = {3}".format(a,b,c,result))


getAnswerDP()