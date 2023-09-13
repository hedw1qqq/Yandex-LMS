def solution(*args, **kwargs):
    print("Как Вас зовут?")
    print(f"Привет, {args[0]}")


def main():
    name = input()
    solution(name)


if __name__ == "__main__":
    main()
