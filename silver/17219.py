import sys
N, M = map(int, sys.stdin.readline().split(' '))
new_dict = dict()
for i in range(N):
    address, password = map(str, sys.stdin.readline().split(' '))
    new_dict[address]=password
for k in range(M):
    address = sys.stdin.readline().split('\n')[0]
    print(new_dict[address].split('\n')[0])
    