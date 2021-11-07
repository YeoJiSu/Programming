A = input()
B = input()
while True:
    try:
        n1 = int(A) * int(B[2])
        n2 = int(A) * int(B[1])
        n3 = int(A) * int(B[0])
        result = n1 + n2*10 + n3*100
        print("{0}\n{1}\n{2}\n{3}".format(n1,n2,n3,result))
        break
    except:
        print("오류가 발생하였습니다.")