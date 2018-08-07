import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as file_object:
        try:
            return json.load(file_object)
        except json.decoder.JSONDecodeError:
            return None


def pretty_print_json(info_pprint):
    pretty_json = json.dumps(info_pprint, indent=4, sort_keys=True, ensure_ascii=False)
    return pretty_json


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        print(pretty_print_json(load_data(filepath)))
    except IndexError:
        sys.exit('Отсутствуют параметры')
    except FileNotFoundError:
        sys.exit('Файл не найден')
    except ValueError:
        sys.exit('В файле нет данных JSON')
