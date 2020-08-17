if __name__ == '__main__':
    s = [9, 7, 8, 3, 2, 1, 5, 6]
    for i in range(s.__len__()):
        if s[i] % 2 == 0:
            s[i] *= 2
    print(s)
