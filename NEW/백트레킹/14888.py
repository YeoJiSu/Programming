# 연산자 끼워넣기
import sys
N = int(sys.stdin.readline())
sequence = list(map(int,sys.stdin.readline().split(' ')))
add,sub,mul,div = map(int,sys.stdin.readline().split(' '))
max_value = -1e9
min_value = 1e9

def dfs(i, num):
    global add, sub, mul, div, max_value, min_value, sequence
    if i == N:
        max_value = max(max_value, num)
        min_value = min(min_value, num)
    else:
        if add > 0 :
            add -= 1
            dfs(i+1,num+sequence[i])
            add += 1
        if sub > 0 :
            sub -= 1
            dfs(i+1,num-sequence[i])
            sub += 1
        if mul > 0 :
            mul -= 1
            dfs(i+1,num*sequence[i])
            mul += 1
        if div > 0 :
            div -= 1
            dfs(i+1,int(num/sequence[i]))
            div += 1
            
dfs(1,sequence[0])

print(max_value)
print(min_value)


