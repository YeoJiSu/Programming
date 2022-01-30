import sys
def mini():
    exp = list(map(str,sys.stdin.readline().split("\n")[0].split("-")))
    new_exp=""
    for i in range(0,len(exp)):
        plus = list(map(int,exp[i].split("+")))
        
        new_exp += str(sum(plus))+"-"
    new_exp = new_exp[:-1]
    print(eval(new_exp))
    
if __name__=="__main__":
    mini()
    

