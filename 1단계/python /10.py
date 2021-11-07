while True:
    try:
        num_array=input()
        num=num_array.split(" ")

        A = int(num[0])
        B = int(num[1])
        C = int(num[2])
        print((A+B)%C)
        print(((A%C) + (B%C))%C)
        print((A*B)%C)
        print(((A%C) * (B%C))%C)
        break
    except:
        print("오류가 발생하였습니다.")