str = input()
list = str.split(" ")
if (int(list[0])==int(list[1])):
    print("==")
elif (int(list[0])<int(list[1])):
    print("<")
else :
    print(">")