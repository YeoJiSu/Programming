import sys
def main():
    weight=[]
    height=[]
    index =[]
    N = int(sys.stdin.readline())
    for i in range(0,N):
        x, y = map(int, sys.stdin.readline().split(" "))
        weight.append(x)
        height.append(y)
        index.append(0)
    
    grade = 1
    i = weight.index(max(weight)) # weight에서 가장 큰 값 index
    index[i]=grade
    
    for k in range(0,N):
        if weight[i] == weight[k]:
            
            
            weight[k]=0
            
        
        
main()

