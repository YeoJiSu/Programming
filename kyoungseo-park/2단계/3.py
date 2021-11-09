def start():
    A = input()
    A = int(A)
    
    # 윤년은 4의 배수, 100의 배수가 아닐 때, 400의 배수일 때 
    # if 4의 배수 and 400의 배수 or not 100 의 배수
    if (A % 4 == 0 and not A % 100 == 0) or (A % 400 == 0):
        print(1)
    else:
        print(0)
    

if __name__ == "__main__":
    start()