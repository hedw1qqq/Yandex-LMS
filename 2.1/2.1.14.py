def solution(*args):
    r, g, b = args
    print(r + b + 1)


def main():
    r = int(input())
    g = int(input())
    b = int(input())
    solution(r, g, b)


if __name__ == "__main__":
    main()