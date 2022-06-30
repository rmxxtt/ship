import json


def load_fields():
    with open('./fields.json') as json_file:
        fields = json.load(json_file)
    return fields


def draw_field(field: dict):
    for y_line in field["field"]:
        for x_value in y_line:
            print(x_value, end=" ")
        print()


def draw_fields(fields: list):
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
