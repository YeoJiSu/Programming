import sys

def count_visible_building(N, buliding):
    if N == 1:
        print(0)
        exit()
    if N == 2:
        print(1)
        exit()
        
    count_visible = [2]*N
    count_visible[0] = 1
    count_visible[-1] = 1

    for i in range(0,N):
        count = 0
        if i!=0:
            front = building[i]-building[i-1]
        length = 1
        for j in range(1,i+1):
            new_val = (building[i]-building[i-j])/length
            if new_val < front:
                count+=1
                front = new_val  
            length += 1
            
        if i!=N-1:
            end = building[i+1]-building[i]
        length = 1
        for k in range(i+1,N):
            new_val = (building[k]-building[i])/length
            if new_val>end:
                count+=1
                end = new_val
            length +=1

        
        count_visible[i] += count
        
    print(max(count_visible))

if __name__ =="__main__":
    N = int(sys.stdin.readline())
    building = list(map(int, sys.stdin.readline().split(" ")))
    count_visible_building(N,building)