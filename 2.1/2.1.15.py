def solution(n: int, m: int, t: int):
    ttime = n * 60 + m + t
    print(str(ttime // 60 % 24).rjust(2, "0") + ":" + str(ttime - 60 * (ttime // 60)).rjust(2, "0"))


def main():
    n = int(input())
    m = int(input())
    t = int(input())
    solution(n, m, t)


if __name__ == "__main__":
    main()
