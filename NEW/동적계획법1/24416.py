import sys
n = int(sys.stdin.readline())
recursiveCount = 0
dynamicCount = 0
f = [1 for _ in range(n+1)]
# 재귀호출 함수
def fib(n):
    global recursiveCount
    if n==1 or n==2:
        recursiveCount+=1
        return 1
    else:
        return fib(n-1)+fib(n-2)
# 동적 프로그래밍 함수
def fibonacci(n):
    global dynamicCount
    for i in range(3,n+1):
        f[i] = f[i-1]+f[i-2]
        dynamicCount+=1
    return f[n]
fib(n)
fibonacci(n)
print(recursiveCount,dynamicCount)