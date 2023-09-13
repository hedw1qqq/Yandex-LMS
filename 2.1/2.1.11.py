def solution(*args, **kwargs):
    a = args
    ans = int(str(a[0])[1] + str(a[0])[0] + str(a[0])[3] + str(a[0])[2])
    print(ans)


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()