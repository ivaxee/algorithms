import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    c = int(input())

    for w in range(c):
        n = int(input())
        a = input().split()
        g_pr = 1
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    pr = 1
                    for m in range(10):
                        if str(m) not in (a[i] + a[j] + a[k]):
                            pr = 0
                            break
                    if pr == 1 and g_pr == 1:
                        print(a[i], a[j], a[k])
                        g_pr = 0
                        break
    pass


if __name__ == '__main__':
    main()
