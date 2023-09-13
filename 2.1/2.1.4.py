def solution(*args, **kwargs):
    a = args
    print(a[0] - round(2.5 * 38))


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
