import sys
import math
def main():
    N = int(sys.stdin.readline())
    X = math.floor(N/5)
    while True:
        if (N-X*5)%3 == 0:
            Y= math.floor((N-X*5)/3)
            break
        else:
            X -=1
        if (X == -1):
            print(-1)
            exit()
    print(X+Y)
main()

# 식 : 5 * X + 3 * Y = N 
# 1. N을 5로 나눈 몫이 X
# 2. N을 5로 나눈 나머지를 3으로 나눈 나머지가 0이라면, 몫이 Y => 끝
# 3. N을 5로 나눈 나머지를 3으로 나눈 나머지가 0이 아니라면, X = X-1 이고 다시 반복문 돌리기
# 4. X 가 -1까지 가면 stop 
    