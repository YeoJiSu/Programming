import sys
def main():
    
    N = int(sys.stdin.readline()) 
    weight=[]
    height=[]
    index = []
    for i in range(0,N):
        x, y = map(int, sys.stdin.readline().split(" "))
        weight.append(x)
        height.append(y)
        index.append(1)
    
    for i in range(0,N):
        for j in range(0,N):
            if weight[i] < weight[j] and height[i] < height[j]:
                index[i]+=1
                
    for i in index:
        print(i,end = " ")
        
main()





