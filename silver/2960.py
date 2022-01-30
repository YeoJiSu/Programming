import sys
def eratosthenes():
    n,k = map(int,sys.stdin.readline().split())
    array = [0]*(n+1)
    count=0
    for i in range(2,n+1):
        array[i]=i
    for i in range(2, n+1):
        if (array[i]==0):
            continue
   
        for j in range(i,n+1,i):
            if array[j]==0:
                continue
            count+=1
            if count==k:
                print(array[j])
                exit()
            array[j]=0
    
if __name__ == "__main__":
    eratosthenes()