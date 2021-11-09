## 이거 답이 뭐임?

def aaaaaaaa():
    a, b = input().split()

    try:
        print(int(a)+int(b))
    except:
        aaaaaaaa()


if __name__ == "__main__":
    aaaaaaaa()