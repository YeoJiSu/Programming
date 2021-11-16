import sys

# a = 개수, b = 최대값
a, b = sys.stdin.readline().split()
a = int(a)
b = int(b)
# 입력받은 a 개의 수
input_list = sys.stdin.readline().split()

if len(input_list) != a:
    assert '입력받은 a와 List의 길이가 다름'

pass_list = []
pass_str = ''
for i in input_list:
    
    if int(i) < b:
        pass_str = pass_str + i + ' '

print(pass_str)
    
