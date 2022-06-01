import sys
S = sys.stdin.readline().split("\n")[0]
arr = list(S)
count = {}

# 0:1, 0:2, 0:3, 0:4, 0:5
# 1:2, 1:3, 1:4, 1:5
# 2:3, 2:4, 2:5,
# 3:4, 3:5
# 4:5
for i in range(len(S)+1):
    for k in range(i+1,len(S)+1):
        value = S[i:k]
        if value not in count:
            count[value]=1
print(len(count))
