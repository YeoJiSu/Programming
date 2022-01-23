import sys
import math
def mod(arr):
    # num = math.ceil(math.sqrt(sorted(arr)[-1]))
    for i in range(2,sorted(arr)[-2]):# 배열중에 젤 작은 애까지 나눠본다
        correct = True
        for k in range(0, len(arr)-1):
            if arr[k]%i != arr[k+1]%i:
                correct = False
                break
        if correct:
            print(i, end = " ")
        

def main():
    num = int(sys.stdin.readline())
    arr = []
    for i in range(0,num):
        a = int(sys.stdin.readline())
        arr.append(a)
    mod(arr)
main()