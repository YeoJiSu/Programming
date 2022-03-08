# 1021
import sys
from collections import deque
def count_number_of_operations(N,my_list):
  total_list = deque(i for i in range(1,N+1))
  count = 0
  for k in my_list:
    while True:
      if total_list[0] == k:
        total_list.popleft()
        break
      else:
        k_index = total_list.index(k)
        middle = len(total_list)//2  # ex) 길이가 3이면 1, 길이가 4면 2
        # k의 인덱스가 중간보다 같거나 작으면 왼쪽으로 이동
        if k_index <= middle:
          while total_list[0] != k:
            total_list.append(total_list.popleft())
            count += 1
        # k의 인덱스가 중간보다 크다면 오른쪽으로 이동
        elif k_index > middle:
          while total_list[0] != k:
            total_list.appendleft(total_list.pop())
            count += 1
  print(count)

if __name__ =="__main__":
  N,M = map(int, sys.stdin.readline().split())
  my_list = list(map(int, sys.stdin.readline().split()))
  count_number_of_operations(N,my_list)