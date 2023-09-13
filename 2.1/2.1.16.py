def solution(*args):
    A, B, C = args
    print(format(round(abs(A - B) / C, 2), '.2f'))


def main():
    A = int(input())
    B = int(input())
    C = int(input())
    solution(A, B, C)


if __name__ == '__main__':
    main()