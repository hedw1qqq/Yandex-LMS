def solution(*args, **kwargs):
    for i in range(3):
        print(*args)


def main():
    n = input()
    solution(n)


if __name__ == '__main__':
    main()
