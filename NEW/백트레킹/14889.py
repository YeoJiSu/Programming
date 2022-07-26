import sys
import itertools
N = int(sys.stdin.readline())
team = []
arr = [ i for i in range(N) ]
for i in range(N):
    team.append(list(map(int, sys.stdin.readline().split(' '))))

comb = list(map(tuple, itertools.combinations(arr,N//2)))
half = comb[:len(comb)//2]
half2 = comb[len(comb)//2:]
del comb
min_value = 1e9

for index in range(len(half)):
    line = half[index]
    line2 = half2[len(half2)-1 - index]
    first = 0
    second = 0
    for x in range(len(line)):
        for y in range(len(line)):
            if x!=y:
                first += team[line[x]][line[y]]
                second += team[line2[x]][line2[y]]
    min_value = min(min_value, abs(first-second))
   
print(min_value)