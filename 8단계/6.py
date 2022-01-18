# 0층 1호(1), 2호(2), 3호(3) 4호(4)
# 1층 1호(1), 2호(3), 3호(6) 4호(10)
# 2층 1호(1), 2호(4), 3호(10) 4호(20)
# 3층 1호(1), 2호(5), 3호(15) 4호(35)
import sys
# N 층 M 호
def count(N, M):
    if (N == 0):
        return M
    sum = 0
    for i in range(1,M+1):
        sum += count(N-1, i)
    return sum
def main():
    num = int(sys.stdin.readline())
    for i in range(0,num):
        N =int(sys.stdin.readline())
        M =int(sys.stdin.readline())
        print(count(N,M))
main()