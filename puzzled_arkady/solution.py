import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    p = float(input())
    print(f"{1/((1-p)*p**2) :.4f}")


if __name__ == '__main__':
    main()
