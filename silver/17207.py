import sys
A_matrix = []
B_matrix = []
people = [["Inseo",0], 
          ["Junsuk",0], 
          ["Jungwoo",0], 
          ["Jinwoo",0], 
          ["Youngki",0]]
for i in range(5):
    A_matrix.append(list(map(int, sys.stdin.readline().split(" "))))
    
for i in range(5):
    B_matrix.append(list(map(int, sys.stdin.readline().split(" "))))

for x in range(5):
    sum_ = 0
    for a in range(5):
        for b in range(5):
            sum_ += A_matrix[x][b]*B_matrix[b][a]
    people[x][1]=sum_
people.reverse()
people = sorted(people, key= lambda x:x[1])
print(people[0][0])