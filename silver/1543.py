import sys
first = sys.stdin.readline().split("\n")[0]
second = sys.stdin.readline().split("\n")[0]
print(len(list(map(str,first.split(second))))-1)