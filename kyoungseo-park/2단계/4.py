def start():
    A = list(input())[0]
    B = list(input())[0]
    
    if not A == '-' and not B == '-':
        print(1)
    elif A == '-' and not B == '-':
        print(2)
    elif A == '-' and B == '-':
        print(3)
    else:
        print(4)
    

if __name__ == "__main__":
    start()