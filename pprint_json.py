import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as file_object:
        try:
            return json.load(file_object)
        except json.decoder.JSONDecodeError:
            return None


def pretty_print_json(python_object):
    pretty_json = json.dumps(python_object, indent=4, sort_keys=True, ensure_ascii=False)
    print(pretty_json)


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        python_object = load_data(filepath)
        pretty_print_json(python_object)
    except IndexError:
        sys.exit('Отсутствуют параметры')
    except FileNotFoundError:
        sys.exit('Файл не найден')
    except ValueError:
        sys.exit('в файле нет данных JSON')
