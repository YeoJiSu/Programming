# N_list를 list로 선언하면 시간초과 에러가 난다. 
# list에서의 in은 리스트의 원소를 하나씩 전부 비교해가면서 찾기 때문에 매우 느리고, 평균적으로 리스트의 길이에 비례하는 시간이 걸린다.
# set은 해시를 사용하기 때문에 평균 상수 시간에 원소를 찾을 수 있다.

import sys
N = int(sys.stdin.readline())
N_list = set(map(int, sys.stdin.readline().split(" ")))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split(" ")))

for k in M_list:
    if k in N_list:
        print(1,end=" ")
    else:
        print(0,end=" ")
        

