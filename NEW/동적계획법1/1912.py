import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split(' ')))
sum_list = []
sum_list.append(n_list[0])

for i in range(1,n):
    sum_list.append(max(sum_list[i-1]+n_list[i],n_list[i]))
    
print(max(sum_list))
