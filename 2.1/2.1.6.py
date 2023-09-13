def solution(*args, **kwargs):
    a = args
    print("Чек")
    print(f'{a[0]} - {a[2]}кг - {a[1]}руб/кг')
    print(f'Итого: {a[2] * a[1]}руб')
    print(f'Внесено: {a[3]}руб')
    print(f'Сдача: {a[3] - a[2] * a[1]}руб')


def main():
    name = input()
    price = int(input())
    weight = int(input())
    money = int(input())
    solution(name, price, weight, money)


if __name__ == '__main__':
    main()