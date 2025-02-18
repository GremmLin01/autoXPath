# XPath Extractor

## Description
This script automatically extracts unique XPath for all visible elements on a web page. It works with Chrome and Firefox browsers, supports multithreading for improved performance, and allows customization of the output file path.

## Requirements
Before using, make sure you have:
- Python 3.7+
- Google Chrome or Mozilla Firefox installed

### Install dependencies

Open a terminal (Mac) or command prompt (Windows) and run:
```sh
pip install -r requirements.txt
```

## Usage

### Running on Windows
Open the command prompt (Win + R → type `cmd` → Enter) and run:
```sh
python script.py "https://example.com" --browser chrome --output xpaths.json
```

### Running on Mac
Open the terminal and run:
```sh
python3 script.py "https://example.com" --browser firefox --output xpaths.json
```

## Command-line arguments
- `url` — required argument, the URL of the web page to analyze.
- `--browser` — choose the browser (`chrome` or `firefox`, default: `chrome`).
- `--output` — specify the output file path (default: `xpaths.json`).

## Example usage

1. Run with Chrome and save to `xpaths.json`:
```sh
python script.py "https://example.com" --browser chrome --output xpaths.json
```

2. Run with Firefox and save to `output.json`:
```sh
python script.py "https://example.com" --browser firefox --output output.json
```

3. Using Python 3 on Mac:
```sh
python3 script.py "https://example.com"
```

## Possible errors and solutions
- **Error: "chromedriver not found" or "geckodriver not found"**
  - Ensure that Chrome or Firefox is installed and drivers are up to date using `webdriver_manager`.

- **Error: "ModuleNotFoundError: No module named 'selenium'"**
  - Ensure all dependencies are installed (`pip install -r requirements.txt`).

## License
This project is licensed under the MIT License.

