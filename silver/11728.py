import sys
N,M = map(int, sys.stdin.readline().split(' '))
N_list = list(map(int,sys.stdin.readline().split(' ')))
M_list = list(map(int,sys.stdin.readline().split(' ')))

new_arr= []
k = min(N,M)
i = 0
j = 0
while True:
    if j==M or i==N :
        break
    if N_list[i] < M_list[j]:
        new_arr.append(N_list[i])
        i+=1
    else:
        new_arr.append(M_list[j])
        j+=1
if j!=M:
    for k in range(j,M):
        new_arr.append(M_list[k])
elif i!=N:
    for k in range(i,N):
        new_arr.append(N_list[k])

for i in new_arr:
    print(i, end=" ")