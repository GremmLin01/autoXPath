import argparse
import json
import logging
import threading
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_xpath(element):
    """Генерация уникального XPath для элемента."""
    try:
        tag = element.tag_name
        if element.get_attribute('id'):
            return f"//{tag}[@id='{element.get_attribute('id')}']"
        if element.get_attribute('class'):
            return f"//{tag}[@class='{element.get_attribute('class')}']"
        parent = element.find_element(By.XPATH, "..")
        siblings = parent.find_elements(By.XPATH, f"./{tag}")
        if len(siblings) == 1:
            return get_xpath(parent) + f'/{tag}'
        else:
            index = siblings.index(element) + 1
            return get_xpath(parent) + f'/{tag}[{index}]'
    except NoSuchElementException:
        return None

def find_all_xpaths(driver):
    """Находит XPath для всех видимых элементов на странице."""
    elements = driver.find_elements(By.XPATH, '//*')
    xpaths = {}
    lock = threading.Lock()
    
    def process_element(el):
        if el.is_displayed() and el.text.strip():
            xpath = get_xpath(el)
            if xpath:
                with lock:
                    xpaths[xpath] = el.text
    
    with ThreadPoolExecutor() as executor:
        executor.map(process_element, elements)
    
    return xpaths

def get_driver(browser):
    """Создает и возвращает драйвер для выбранного браузера."""
    try:
        options = None
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        else:
            raise ValueError("Unsupported browser. Choose 'chrome' or 'firefox'.")
    except WebDriverException as e:
        logging.error(f"Error initializing the WebDriver: {e}")
        return None

def main(url, browser, output_file):
    """Запускает браузер, анализирует страницу и сохраняет XPath в файл."""
    logging.info(f"Starting browser ({browser}) for URL: {url}")
    driver = get_driver(browser)
    if not driver:
        logging.error("Failed to initialize the WebDriver. Exiting.")
        return
    
    try:
        driver.get(url)
        xpaths = find_all_xpaths(driver)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(xpaths, f, ensure_ascii=False, indent=4)
        logging.info(f"XPaths saved to {output_file}.")
    except WebDriverException as e:
        logging.error(f"Error loading page: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract XPaths from a web page.")
    parser.add_argument("url", type=str, help="URL of the page to analyze")
    parser.add_argument("--browser", type=str, choices=["chrome", "firefox"], default="chrome", help="Browser to use (default: chrome)")
    parser.add_argument("--output", type=str, default="xpaths.json", help="Output file (default: xpaths.json)")
    args = parser.parse_args()
    
    main(args.url, args.browser, args.output)


#Запуск скрипта
#python script.py "https://example.com" --browser firefox --output results.json
