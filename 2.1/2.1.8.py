def solution(*args, **kwargs):
    for i in range(args[0]):
        print(f'Я больше никогда не буду писать "{args[1]}"!')


def main():
    N = int(input())
    message = input()
    solution(N, message)


if __name__ == '__main__':
    main()
