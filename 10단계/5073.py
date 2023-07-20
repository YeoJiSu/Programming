# 백준 5073번 - 삼각형과 세 변
import sys
while True:
    A,B,C = map(int, sys.stdin.readline().split(' '))
    if A==B==C==0:
        exit()
    if A==B==C:
        print("Equilateral")
    elif (A+B<=C or A+C<=B or B+C<=A):
        print("Invalid")
    elif A==B or A==C or B==C:
        print("Isosceles")
    else:
        print("Scalene")