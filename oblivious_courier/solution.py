import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, k = map(int, input().split())
    print(1/n)


if __name__ == '__main__':
    main()
