import sys
def price():
    num = int(sys.stdin.readline())
    for i in range(num):
        my_list = []
        while True:
            earth = int(sys.stdin.readline())
            if earth==0:
                break
            my_list.append(earth)
        sum = 0
        my_list.sort(reverse=True)
        for i in range(len(my_list)):
            sum+=2*(my_list[i]**(i+1))
        if sum > 5*(10**6):
            print("Too expensive")
        else:
            print(sum)
if __name__ == "__main__":
    price()