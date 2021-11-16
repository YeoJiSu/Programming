def aaaaaaaa():
    A, B, C = input().split()
    A, B, C = int(A), int(B), int(C)

    try:
        print((A+B)%C)
        print(((A%C) + (B%C))%C)
        print((A*B)%C)
        print( ((A%C) * (B%C))%C)
    except:
        aaaaaaaa()


if __name__ == "__main__":
    aaaaaaaa()