import sys


def sort_by_age():
    num = int(sys.stdin.readline())
    my_array = []
    for i in range(num):
        age, name = sys.stdin.readline().split("\n")[0].split(" ")
        my_array.append([int(age), name])

    c = sorted(my_array, key = lambda x:x[0])
    for i in c:
        print(i[0], i[1])


if __name__ == "__main__":
    sort_by_age()
