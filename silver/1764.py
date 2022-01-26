import sys
a,b = map(int,sys.stdin.readline().split(" "))
A = []
B = []
for i in range(0,a):
    name = sys.stdin.readline()
    A.append(name)
for i in range(0,b):
    name = sys.stdin.readline()
    B.append(name)
inter = list(set(A)&set(B))
print(len(inter))
for i in sorted(inter):
    print(i.split("\n")[0])