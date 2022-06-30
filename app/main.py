import json
import enum


class Ship(enum.Enum):
    # Если корабль больше 1х1, его стороны по длине должны быть равны друг другу
    MIN = 1  # минимальный длина корабля корабль 1х1
    MAX = 4  # максимальная длина стороны корабля


def load_fields():
    # Загружаем поля
    with open('./fields.json') as json_file:
        fields = json.load(json_file)
    return fields


def draw_field(field: dict):
    # Выводим поле
    for y_line in field["field"]:
        for x_value in y_line:
            print(x_value, end=" ")
        print()


def draw_fields(fields: list):
    # Выводим поля из списка
    for field in fields:
        for y_line in field["field"]:
            for x_value in y_line:
                print(x_value, end=" ")
            print()
        print()


def main():
    data = load_fields()


if __name__ == '__main__':
    main()
