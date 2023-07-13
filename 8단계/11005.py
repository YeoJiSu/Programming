# 백준 11005번 - 진법 변환 2
import sys

N, B = sys.stdin.readline().split('\n')[0].split(' ')
N = int(N)
B = int(B)

answer = ""

while True:
    mod = N%B
    if mod >=10:
        mod = chr(mod+55)
    mod = str(mod)
    answer = mod + answer
    N = N//B
    if N < B:
        if N >=10:
            N = chr(N+55)
        else:
            N = str(N)
        answer = N + answer
        break
print(answer)
