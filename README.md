# Prettify JSON

Скрипт выводит содержимое файла JSON в консоль в удобном для чтения виде: добавляет переносы строк, отступы слева и пробелы.

# Quickstart

Для запуска скрипта необходимо в строке команд текущей директории прописать название файла-скрипта и файла-JSON

```bash

$ python pprint_json.py <filepath/to/.json>
```
Например, 
```bash
$ python pprint_json.py alko.json
```

# Пример ответа скрипта
```bash
[
   {
        "Address": "Головинское шоссе, дом 5, корпус 1",
        "AdmArea": "Северный административный округ",
        "District": "Головинский район",
        "ID": "00151088",
        "IsNetObject": "нет",
        "Latitude_WGS84": "55.8412678991196860",
        "Longitude_WGS84": "37.4937817305074500",
        "Name": "Вино и бочка",
        "PublicPhone": [
            {
                "PublicPhone": "(495) 916-93-88"
            }
        ],
        "TypeObject": "Магазин «Алкогольные напитки»",
        "TypeService": "реализация продовольственных товаров",
        "WorkingHours": [
            {
                "DayOfWeek": "понедельник",
                "Hours": "10:00-22:00"
            },
            {
                "DayOfWeek": "вторник",
                "Hours": "10:00-22:00"
            },
            {
                "DayOfWeek": "среда",
                "Hours": "10:00-22:00"
            },
            {
                "DayOfWeek": "четверг",
                "Hours": "10:00-22:00"
            },
            {
                "DayOfWeek": "пятница",
                "Hours": "10:00-22:00"
            },
            {
                "DayOfWeek": "суббота",
                "Hours": "10:00-22:00"
            },
            {
                "DayOfWeek": "воскресенье",
                "Hours": "10:00-22:00"
            }
        ],
        "geoData": {
            "coordinates": [
                37.49378173050745,
                55.841267899119686
            ],
            "type": "Point"
        },
        "global_id": 638497406
    }
]
``` 

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
