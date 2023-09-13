def solution(sweets: int, kids: int):
    print(sweets // kids)
    print(sweets - sweets // kids * kids)


def main():
    kids = int(input())
    sweets = int(input())
    solution(sweets, kids)


if __name__ == "__main__":
    main()