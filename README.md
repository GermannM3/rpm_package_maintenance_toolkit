# RPM Package Maintenance Toolkit

Инструментарий для автоматизации создания и обновления RPM пакетов.

## Оглавление
- [Установка](#установка)
- [Использование](#использование)
- [Тестирование](#тестирование)
- [Структура проекта](#структура-проекта)
- [Лицензия](#лицензия)

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/yourusername/rpm_package_maintenance_toolkit.git
   cd rpm_package_maintenance_toolkit

   
2.
Установите необходимые зависимости:


pip3 install -r requirements.txt


Использование

Создание RPM пакета


python3 scripts/create_rpm.py path/to/example.spec path/to/output_directory

Обновление RPM пакета


python3 scripts/update_rpm.py path/to/example.spec new_version path/to/output_directory


Тестирование


Для запуска тестов, выполните:

python3 -m unittest discover -s tests

Структура проекта

rpm_package_maintenance_toolkit/
├── scripts/
│   ├── create_rpm.py
│   └── update_rpm.py
├── examples/
│   └── example_package/
│       ├── example.spec
│       └── example_script.sh
├── tests/
│   └── test_create_rpm.py
├── README.md
└── requirements.txt

Лицензия

MIT License

Copyright (c) 2025 GermannM

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
# rpm_package_maintenance_toolkit
