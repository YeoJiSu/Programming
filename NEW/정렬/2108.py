# 2108번 - 통계학
import sys
from collections import Counter
N = int(sys.stdin.readline())
arr = []
for i in range(0,N):
    arr.append(int(sys.stdin.readline()))
print(round(sum(arr)/N)) # 산술평균
arr.sort()
print(arr[N//2]) # 중앙값

# # 최빈값
# count = []
# for k in arr:
#     value = [k,arr.count(k)]
#     if value not in count:
#         count.append(value)
# count.sort(key=lambda x:-x[1])
# if (N==1):
#     print(arr[0])
# else:
#     if (count[0][1]!=count[1][1]):
#         print(count[0][0])
#     else:
#         print(count[1][0])
# # => 시간 초과 나는 코드임.

# 최빈값 : collections 모듈의 Counter 클래스 사용하기
new_arr = Counter(arr).most_common()
if (len(new_arr)==1):
    print(new_arr[0][0])
else:
    if (new_arr[0][1]==new_arr[1][1]):
        print(new_arr[1][0])
    else:
        print(new_arr[0][0])
print(arr[N-1]-arr[0]) # 범위