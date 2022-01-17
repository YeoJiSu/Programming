import sys

def main():
    N, M  = map(int, sys.stdin.readline().split(" "))
    my_array = []
    for i in range(0,N):
        my_array.append(sys.stdin.readline().split("\n")[0])

    new_1 = N*M
    new_2 = N*M
    
    for j in range(0,N-8+1):
        for f in range(0,M-8+1):         
            count_1 = 0
            count_2 = 0      
            for i in range(j,j+8):
                for k in range(f,f+8):
                    if (i%2==0 and k%2==0) or (i%2!=0 and k%2!=0):
                        if (my_array[i][k]!="W"):
                            count_1+=1
                        else : # "B" 가 아니라면
                            count_2+=1
                    else :
                        if (my_array[i][k]!="B"):
                            count_1+=1
                        else : # "W" 가 아니라면
                            count_2+=1
            if (count_1 < new_1):  
                new_1 = count_1
            elif (count_2 < new_2):
                new_2 = count_2
    if (new_1 < new_2):
        print(new_1)
    else:
        print(new_2) 
                
    
        
main()





