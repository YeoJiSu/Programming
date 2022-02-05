import sys
def reverse_string():
    my_input = sys.stdin.readline().split("\n")[0]
    my_list = list(map(str, my_input.split("<")))
    new_string=""
    for i in my_list:
        if i=="":
            continue
        
        if ">" in i:
            a, b = i.split(">")
            new_list = list(map(str, b.split(" ")))
            string=""
            for j in new_list:
                string+=j[::-1]+" "
            new_string+="<"+a+">"+string[:-1]
        else:
            new_list = list(map(str, i.split(" ")))
            string=""
            for j in new_list:
                string+=j[::-1]+" "
            new_string+=string[:-1]
    print(new_string)
            
if __name__=="__main__":
    reverse_string()