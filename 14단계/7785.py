# 백준 7785번: 회사에 있는 사람
import sys
n = int(sys.stdin.readline())
enter = set()
for i in range(n):
    a, b = sys.stdin.readline().split("\n")[0].split(' ')
    if b=='enter':
        enter.add(a)
    else:
        enter.remove(a)
answer = list(enter)
answer.sort(reverse=True)
for i in answer:
    print(i) 
"""  
리스트에서의 x in s 연산의 평균 시간 복잡도 : O(n)
세트에서의 x in s 연산의 평균 시간 복잡도 : O(1)
* 세트가 효율적인 이유 = 해시 테이블 (파이썬에서는 세트가 해시 테이블(hash table)로 구현되어있다!!)

"""  