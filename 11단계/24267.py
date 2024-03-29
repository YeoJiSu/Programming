# 백준 24267번 : 알고리즘 수업 - 알고리즘의 수행 시간 6
import sys
n = int(sys.stdin.readline())
print((n*(n-1)*(n-2))//6)
print(3)


"""
i = 1 일 때,   n-2 + n-3 + n-4 + ... + 2 + 1
i = 2 일 때,         n-3 + n-4 + ... + 2 + 1
i = 3 일 때,               n-4 + ... + 2 + 1
...
i = n-1 일 때,                         2 + 1
i = n-2 일 때,                             1 

따라서 위를 식으로 세워보면, 
f(n) = 1*(n-2) + 2*(n-3) + 3*(n-4) + ... + (n-3)*2 + (n-2)*1
     = ∑ k*(n-1-k)  이때 k는 1부터 n-2까지
     = ∑ -k^2 +(n-1)*k
     = -(n-2)*(n-1)*(2n-3)/6 + (n-1)*((n-2)*(n-1)/2)
     = (n-2)*(n-1)*{ (-2n+3)/6 + (3n-3)/6 }
     = (n-2)*(n-1)*(n/6)
     = (n*(n-1)*(n-2))//6
"""