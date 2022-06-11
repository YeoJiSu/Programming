import sys
N, M = map(int, sys.stdin.readline().split(' '))
arr = list(map(int, sys.stdin.readline().split(' ')))

# M으로 나눈 나머지 0,1,2.. 각각의 개수
count = [0 for i in range(M)] 

# 나머지 배열의 첫항 구하기
arr[0] = arr[0]%M
count[arr[0]]+=1

# 누적합 구하기
for i in range(N-1):
    arr[i+1] = (arr[i+1]%M + arr[i])%M
    count[arr[i+1]]+=1

# 나머지 0 인게 선택되었을때
result = count[0] 
for i in count:
    if i>1:
        # 나머지가 같은 것들끼리 선택되었을때 
        result+= i * (i-1) // 2  

print(result)

