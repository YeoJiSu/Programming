import math
time = input()
hour = int(time.split(" ")[0])
minute = int(time.split(" ")[1])
total =  hour*60 +minute - 45
if (total<0):
    total+=60*24    
    

print("{0} {1}".format(math.trunc(total/60), total%60))
