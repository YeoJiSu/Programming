import sys

def shortest_path(x,y,w,h):
    my_path = [abs(x-0), abs(x-w), abs(y-0), abs(y-h)]
    print(min(my_path))
def main():
    x,y,w,h = map(int, sys.stdin.readline().split(" "))
    shortest_path(x,y,w,h)
main()