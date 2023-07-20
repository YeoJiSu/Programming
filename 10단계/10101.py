# 백준 10101번 - 삼각형 외우기
import sys
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
if A==B==C==60:
    print("Equilateral")
elif (A+B+C == 180) and (A==B or A==C or B==C):
    print("Isosceles")
elif A+B+C == 180:
    print("Scalene")
else:
    print("Error")