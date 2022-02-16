import sys
N, M = map(int, sys.stdin.readline().split(' '))
my_list = []
for i in range(N):
    my_list.append(sys.stdin.readline().split("\n")[0])
new_str=""
count = 0
for i in range(M):
    ATGC_list = ['A','C','G','T']
    ATGC_index = [0,0,0,0]
    for j in range(N):
        ATGC_index[ATGC_list.index(my_list[j][i])]+=1
    my_index =max(ATGC_index)
    new_str+=ATGC_list[ATGC_index.index(my_index)]
    for j in ATGC_index:
        if j!=0:
            count+=j
    count-=my_index
print(new_str)
print(count)

