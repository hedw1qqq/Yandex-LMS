def solution(*args, **kwargs):
    a = args
    print(a[2] - a[0] * a[1])


def main():
    price = int(input())
    weight = int(input())
    money = int(input())
    solution(price, weight, money)


if __name__ == '__main__':
    main()
