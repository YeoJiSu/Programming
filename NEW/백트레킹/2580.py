# 스도쿠
import sys
sudoku = []
zero = []
for i in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().split(' '))))
for i in range(9):
    for k in range(9):
        if sudoku[i][k]==0:
            zero.append([i,k])
def possibleWidth(x,num):
    # x번째 가로줄에 num이 들어갈 수 있는지
    for i in range(9):
        if sudoku[x][i] == num:
            return False
    return True

def possibleVertical(y,num):
    # y번째 세로줄에 num이 들어갈 수 있는지
    for i in range(9):
        if sudoku[i][y] == num:
            return False
    return True
    
def possibleSquare(x,y,num):
    # (x,y)가 속한 정사각형에 num 이 들어갈 수 있는지
    x = x//3 * 3
    y = y//3 * 3
    for nx in range(3):
        for ny in range(3):
            if sudoku[x+nx][y+ny] == num:
                return False
    return True

def backTracking(count):
    if count == len(zero):
        for line in sudoku:
            print(*line)
        exit(0)
    else:
        x = zero[count][0]
        y = zero[count][1]
        for num in range(1,10):
            if possibleWidth(x,num) and possibleVertical(y,num) and possibleSquare(x,y,num):
                sudoku[x][y] = num
                backTracking(count+1)
                sudoku[x][y] = 0
backTracking(0)

