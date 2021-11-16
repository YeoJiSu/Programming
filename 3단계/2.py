count=int(input())
for i in range(0, count):
    str= input()
    sum= int(str.split(" ")[0]) + int(str.split(" ")[1])
    print(sum)