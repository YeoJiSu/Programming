def d(n):
    return n+sum(list(map(int,str(n)))) 

def main():
    a = list(range(1,10000))
    for i in range(1,10000):
        if d(i) in a:
             a.remove(d(i))
    for j in range(0,len(a)):
        print(a[j])
main()