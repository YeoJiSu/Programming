import sys

def main():
    try:
        my_list =list(map(str,sys.stdin.readline().split("\n")[0]))
        count_alpha(my_list)
    except:
        exit()

def count_alpha(str):
    if len(str)<=1:
        print(len(str))
    else:
        len1 = len(str)
        for i in range(1, len(str)):
            if str[i]=="-":
                if str[i-1]=="c" or str[i-1]=="d":
                    len1-=1 # len 감소 
                    i+=1 # index 증가시키기 
            elif str[i]=="j":
                if str[i-1]=="l" or str[i-1]=="n":
                    len1-=1 # len 감소 
                    i+=1 # index 증가시키기 
            elif str[i]=="=":
                if str[i-1]=="c" or str[i-1]=="s":
                    len1-=1 # len 감소 
                    i+=1 # index 증가시키기   
                elif str[i-1]=="z":
                    if i-2>=0 and str[i-2]=="d":
                        len1-=1 # len 감소 
                        i+=1 # index 증가시키기 
                    len1-=1 # len 감소 
                    i+=1 # index 증가시키기 
        print(len1)
main()

# list로 만든 후

                
        
# "c-"
# "d-"
# "lj"
# "nj"
# "dz="
# "c="
# "s="
# "z="

        
        