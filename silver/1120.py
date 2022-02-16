import sys
def diff():
    A,B = sys.stdin.readline().split("\n")[0].split(" ")
    dif = len(B)-len(A)
    result = len(B)
    plus=""
    new_A = A
    for i in range(0,dif+1):
        count = 0
        for j in range(len(new_A)):
            if new_A[j]!=B[j]:
                count+=1
        if count<result:
            result = count
        plus+=B[i]
        new_A = plus+A
    print(result)
if __name__ == "__main__":
    diff()