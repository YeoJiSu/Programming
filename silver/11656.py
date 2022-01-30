import sys
def suffix():
    my_string = sys.stdin.readline().split("\n")[0]
    my_array = []
    for i in range(len(my_string)):
        my_array.append(my_string[i:])
    print(*sorted(my_array),sep="\n")

if __name__ == "__main__":
    suffix()