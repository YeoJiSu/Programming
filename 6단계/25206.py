# [2022 인하대학교 프로그래밍 경진대회(IUPC) B번] 너의 평점은

import sys
grade_standard = {
    'A+':4.5,
    'A0':4.0,
    'B+':3.5,
    'B0':3.0,
    'C+':2.5,
    'C0':2.0,
    'D+':1.5,
    'D0':1.0,
    'F' :0.0,
}


average_score = 0
div_score = 0
for i in range(20):
    subject_name, grades, score = sys.stdin.readline().split("\n")[0].split(" ")
    grades = float(grades)
    if score == 'P':
        continue
    div_score+=grades
    average_score += grades*grade_standard[score]

# 소수점 반올림
print(round(average_score/div_score,6))