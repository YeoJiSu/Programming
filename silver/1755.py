import sys
my_num = [[0,"zero"],[1,"one"],[2,"two"],[3,"three"],[4,"four"],[5,"five"],
 [6,"six"],[7,"seven"],[8,"eight"],[9,"nine"]]
def dictionary():
    M,N = map(int, sys.stdin.readline().split(" "))
    new_dic = []
    for i in range(M, N+1):
        front_num = list(str(i))
        my_str=""
        for j in front_num:
            my_str+=my_num[int(j)][1]
            
        new_dic.append([my_str,i])
    new_dic.sort()
    len = 0
    for k in new_dic:
        print(k[1],end=" ")
        if (len+1)%10 == 0:
            print()
        len+=1
    
if __name__ == "__main__":
    dictionary()