def solution(*args, **kwargs):
    for i in range(*args):
        print('Купи слона!')


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()