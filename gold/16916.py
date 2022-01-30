import sys
def compare():
    my_str = sys.stdin.readline().split("\n")[0]
    split_str = sys.stdin.readline().split("\n")[0]
    if len(my_str.split(split_str))==1:
        print(0)
    else:
        print(1)
          
if __name__ == "__main__":
    compare()