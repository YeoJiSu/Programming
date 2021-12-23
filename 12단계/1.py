import sys
def main():
    num = int(sys.stdin.readline())
    arr=[]
    for i in range(num):
        arr.append(int(sys.stdin.readline()))
    for i in sort(arr):
        print(i)
  
    
# 삽입정렬 8 5 6 4 2  -> 5 8 6 4 2 
def sort(arr):
    for i in range(1, len(arr)):
        com = arr[i] # arr[2] = 6
        j = i-1  # j = 1
        
        while j>=0 and arr[j] > com:
            arr[j+1]=arr[j] #  arr[2] = arr[1]
            j-=1
            
        arr[j+1] = com
            
    return arr
    
main()

