def solution(n: int, m: int, k1: int, k2: int):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (i + j == n) and (k1 * i + k2 * j == n * m):
                print(i, j)


def main():
    n = int(input())
    m = int(input())
    k1 = int(input())
    k2 = int(input())
    solution(n, m, k1, k2)


if __name__ == "__main__":
    main()
