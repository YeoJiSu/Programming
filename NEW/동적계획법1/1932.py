import sys
n = int(sys.stdin.readline())
n_list = []
for i in range(n):
    n_list.append(list(map(int,sys.stdin.readline().split(' '))))

for i in range(1,n):
    for j in range(i+1):
        if j == 0: 
            n_list[i][j]+=n_list[i-1][j]
        elif j == i :
            n_list[i][j]+=n_list[i-1][j-1]
        else:
            n_list[i][j]+=max(n_list[i-1][j-1],n_list[i-1][j])
        
        
print(n_list)
print(max(n_list[n-1]))