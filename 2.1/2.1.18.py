def solution(price: str, kup: int):
    print(kup - int(price, 2))


def main():
    price = input()
    kup = int(input())
    solution(price, kup)


if __name__ == '__main__':
    main()