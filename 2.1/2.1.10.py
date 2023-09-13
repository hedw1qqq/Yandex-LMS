def solution(name: str, number: int):
    print(f"Группа №{number // 100}.")
    print(f"{number % 10}. {name}.")
    print(f"Шкафчик: {number}.")
    print(f"Кроватка: {number // 10 % 10}.")


def main():
    name = input()
    number = int(input())
    solution(name, number)


if __name__ == "__main__":
    main()