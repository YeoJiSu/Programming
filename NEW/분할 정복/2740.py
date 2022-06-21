import sys
AN, AM = map(int,sys.stdin.readline().split(' '))
listOfA = []
for i in range(AN):
    listOfA.append(list(map(int,sys.stdin.readline().split(' '))))
BN, BM = map(int,sys.stdin.readline().split(' '))
listOfB = []
for i in range(BN):
    listOfB.append(list(map(int,sys.stdin.readline().split(' '))))


# for i in range(AN):
#     for k in range(AN):
#         total = 0
#         for j in range(AM):
#             total += listOfA[i][j]*listOfB[j][k]
#         print(total,end=" ")
#     print()
for i in range(AN):
    for j in range(BM):
        total = 0
        for k in range(AM):
            total += listOfA[i][k] * listOfB[k][j]
        print(total,end=" ")
    print()