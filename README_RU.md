# XPath Extractor

## Описание
Этот скрипт автоматически извлекает уникальные XPath всех видимых элементов на веб-странице. Работает с браузерами Chrome и Firefox, поддерживает многопоточную обработку для повышения производительности, а также позволяет настраивать путь сохранения результата.

## Требования
Перед использованием убедитесь, что у вас установлены:
- Python 3.7+
- Google Chrome или Mozilla Firefox

### Установка зависимостей

Откройте терминал (Mac) или командную строку (Windows) и выполните:
```sh
pip install -r requirements.txt
```

## Использование

### Запуск на Windows
Откройте командную строку (Win + R → введите `cmd` → Enter) и выполните команду:
```sh
python script.py "https://example.com" --browser chrome --output xpaths.json
```

### Запуск на Mac
Откройте терминал и выполните команду:
```sh
python3 script.py "https://example.com" --browser firefox --output xpaths.json
```

## Аргументы командной строки
- `url` — обязательный аргумент, URL-адрес веб-страницы для анализа.
- `--browser` — выбор браузера (`chrome` или `firefox`, по умолчанию `chrome`).
- `--output` — путь к файлу для сохранения результатов (`xpaths.json` по умолчанию).

## Примеры использования

1. Запуск с Chrome и сохранение в `xpaths.json`:
```sh
python script.py "https://example.com" --browser chrome --output xpaths.json
```

2. Запуск с Firefox и сохранение в `output.json`:
```sh
python script.py "https://example.com" --browser firefox --output output.json
```

3. Использование Python 3 в Mac:
```sh
python3 script.py "https://example.com"
```

## Возможные ошибки и их решения
- **Ошибка: "chromedriver not found" или "geckodriver not found"**
  - Убедитесь, что установлены Chrome или Firefox и обновлены драйверы через `webdriver_manager`.

- **Ошибка: "ModuleNotFoundError: No module named 'selenium'"**
  - Убедитесь, что установлены все зависимости (`pip install -r requirements.txt`).

## Лицензия
Этот проект распространяется под лицензией MIT.

