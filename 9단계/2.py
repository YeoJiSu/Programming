import sys
M= int(sys.stdin.readline())
N= int(sys.stdin.readline())
m_list = []
count = 0
for j in range(M,N+1):
    if j==1:
        count =0
    elif j==2:
        m_list.append(j)
    else:
        num=j
        for k in range(2,j-1):
            if j%k==0:
                num =0
                break
        if num!=0:
            m_list.append(num)
if len(m_list)==0:
    print(-1)
else:
    print(sum(m_list))
    print(m_list[0])

