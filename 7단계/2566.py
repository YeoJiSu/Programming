# 백준 2566번 - 최댓값
import sys

_max = 0
_max_index = [1,1]
for i in range(9):
    _list = list(map(int, sys.stdin.readline().split(' ')))
    for j in range(9):
        if _list[j] > _max:
            _max = _list[j]
            _max_index = [i+1,j+1]

print(_max)
print(*_max_index)