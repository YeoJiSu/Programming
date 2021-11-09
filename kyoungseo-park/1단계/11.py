def aaaaaaaa():
    A = int(input())
    B = input()
    
    B3 = A * int(B[2])
    B4 = A * int(B[1])
    B5 = A * int(B[0])
    B6 = A * int(B)


    try:
        print(B3, B4, B5, B6, sep='\n')
    except:
        aaaaaaaa()


if __name__ == "__main__":
    aaaaaaaa()