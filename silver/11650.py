import sys


def sort_location():
    num = int(sys.stdin.readline())
    my_array = []
    for i in range(num):
        a, b = map(int, sys.stdin.readline().split(" "))
        my_array.append([a, b])
    my_array.sort()
    for i in my_array:
        print(i[0], i[1])


if __name__ == "__main__":
    sort_location()
