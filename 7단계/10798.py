# 10798: 세로읽기
import sys
_list = [[""for i in range(15)]for j in range(5)]

for i in range(5):
    new_list = list(sys.stdin.readline().split("\n")[0])
    for j in range(len(new_list)):
        _list[i][j] = new_list[j]


for i in range(15):
    for j in range(5):
        print(_list[j][i], end="")