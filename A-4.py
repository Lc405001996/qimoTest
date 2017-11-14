def tuzi(n):
    if n <= 1:
        return 2
    else:
        return 2 * tuzi(n - 2)


if __name__ == '__main__':
    n = int(input('请输入月数（整数）：'))
    print(tuzi(n))
