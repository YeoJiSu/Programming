def aaaaaaaa():
    a, b = input().split()
    a = int(a)
    b = int(b)
    try:
        print(a+b)
        print(a-b)
        print(a*b)
        print(str(a/b).split('.')[0])
        print(a%b)
    except:
        aaaaaaaa()


if __name__ == "__main__":
    aaaaaaaa()