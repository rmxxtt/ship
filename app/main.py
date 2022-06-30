import json


def load_fields():
    with open('./fields.json') as json_file:
        fields = json.load(json_file)
    return fields


def draw_field(field: dict):
    for xy in field["field"]:
        for value in xy:
            print(value, end=" ")
        print()


def draw_fields(fields: list):
    for field in fields:
        for xy in field["field"]:
            for value in xy:
                print(value, end=" ")
            print()
        print()


def main():
    data = load_fields()


if __name__ == '__main__':
    main()
