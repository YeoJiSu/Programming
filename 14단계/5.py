import sys

count = 0

def main():
    num = int(sys.stdin.readline())
    col = [0] * (num+1) # 9
    n_queens(0,col)
    print(count)
    
def n_queens(i, col):
    n = len(col)-1 # 8
    
    if (is_correct(i,col)):
        if i == n:
            global count
            count+=1
        else:
            for j in range(1, n+1): # 1부터 8까지 넣어보는겨
                col[i+1] = j
                n_queens(i+1,col)

def is_correct(i, col):
    k = 1
    while k<i:
        if (col[i]==col[k] or abs(col[i]-col[k])==i-k):
            return False
        k+=1
    return True
main()