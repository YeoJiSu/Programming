# 5430
import sys
from collections import deque

def AC_language(T):
  for i in range(T):
    p = sys.stdin.readline().split("\n")[0]
    n = int(sys.stdin.readline())
    my_list = deque(eval(sys.stdin.readline()))
    not_error = True
    reverse = 0
    for j in p:
      if j == "R":
        reverse+=1
      elif j == "D":
        if len(my_list) == 0:
          print("error")
          not_error = False
          break
        elif reverse%2 == 0:
          my_list.popleft()
        elif reverse%2 == 1:
          my_list.pop()
    if (not_error):
      if (reverse%2 == 1):
        my_list.reverse()
      print(str(list(my_list)).replace(' ',''))
if __name__ == "__main__":
  T = int(sys.stdin.readline())
  AC_language(T)
