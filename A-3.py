import sys


def bubbleSort(a):
    for i in range(len(a) - 1, -1, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            #print(a)


def main():
    a = []
    for i in range(1,len(sys.argv)):
        a.append(int(sys.argv[i]))
    bubbleSort(a)
    print(a)


if __name__ == '__main__':
    main()
