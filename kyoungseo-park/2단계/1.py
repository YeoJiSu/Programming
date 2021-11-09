def aaaaaaaa():
    A, B = input().split()
    A = int(A)
    B = int(B)
    
    if A < B:
        print('<')
    elif A > B:
        print('>')
    elif A == B:
        print('==')

if __name__ == "__main__":
    aaaaaaaa()