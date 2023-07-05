# 백준 10988번: 팰린드롬인지 확인하기

import sys

word = sys.stdin.readline().split("\n")[0]

length = len(word)

for i in range(0, length//2):
    if word[i] != word[length-1-i]:
        print(0)
        exit()
    
print(1)