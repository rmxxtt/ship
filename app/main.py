import json
import enum


class Ship(enum.Enum):
    # Если корабль больше 1х1, его стороны по длине должны быть равны друг другу
    MIN = 1  # минимальный длина корабля корабль 1х1
    MAX = 4  # максимальная длина сторон корабля


class LineDirection(enum.Enum):
    # Направление стороны корабля для функции поиска
    LEFT = 1
    RIGHT = 2
    TOP = 3
    BOTTOM = 4


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


def is_outside_field(x, y, h, w) -> bool:
    # Проверяем, выходят ли координаты за пределы поля
    if (0 > x > w) or (0 > y > h):
        return False
    else:
        return True


def walk_the_line(X: int, Y: int, direction: LineDirection, field: dict):
    to_x = 0
    to_y = 0
    match direction:
        case LineDirection.LEFT:
            to_x -= 1
        case LineDirection.RIGHT:
            to_x += 1
        case LineDirection.TOP:
            to_y -= 1
        case LineDirection.BOTTOM:
            to_y += 1
    x = X + to_x
    y = Y + to_y
    if not is_outside_field(x, y, field["h"], field["w"]):
        pass


def algorithm_1(field: dict):
    for Y in range(field["h"]):
        for X in range(field["w"]):
            # Если * - начинаем двигаться по сторонам
            if field["field"][Y][X] == "*":
                # Влево
                y, x = Y, X - 1
                if x >= 0:
                    pass


def main():
    data = load_fields()
    algorithm_1(data[1])


if __name__ == '__main__':
    main()
