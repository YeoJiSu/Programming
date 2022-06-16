import sys
N = int(sys.stdin.readline())

p_list = [1,1,1,2,2]

for i in range(95):
    p_list.append(p_list[4+i] + p_list[i])
   

for i in range(N):
    a = int(sys.stdin.readline())
    print(p_list[a-1])
    
    
# 1 1 1 2 2 3 4 5 7 9 12 16

# 1
# 1
# 1
# 2
# 2
# 2+ 1 = 3
# 3+ 1 = 4
# 4+ 1 = 5
# 5 + 2 = 7
# 7 + 2 = 9
# 9 + 3 = 12
# 12+ 4 = 16
# 16+ 5 = 21
# 21+ 7 = 28
# 28 + 9 = 37
