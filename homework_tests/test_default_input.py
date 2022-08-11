from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyperclip
from selenium.webdriver.common.by import By
from time import sleep

s = Service("/usr/local/bin/chromedriver")
chrome_driver = webdriver.Chrome(service=s)
chrome_driver.get("https://rioran.github.io/ru_vowels_filter/main.html")

# Test data

default_input_text = """Сменялись в детстве радугой дожди,
Сияньем солнца — сумрачные тени.
Но в зрелости не требуй и не жди
Таких простых и скорых утешений.

Самуил Яковлевич Маршак"""

default_output_vowels = """еяиееауоои
ияеоауаыееи
оеоиееуиеи
аиоыиоыуееи

ауияоеиаа"""

default_output_vowels_whitespace = """еяи ее ауо ои
ияе оа уаые еи
о еои е еу и е и
аи оы и оы уееи

ауи яоеи аа"""

default_output_vowels_whitespace_symbols = """еяи ее ауо ои,
ияе оа уаые еи.
о еои е еу и е и
аи оы и оы уееи.

ауи яоеи аа"""


def test_check_button_size_adjustment():
    sleep(5)
    chrome_driver.maximize_window()
    width_before = chrome_driver.find_element(By.CSS_SELECTOR, ".btn-success").value_of_css_property('width')
    chrome_driver.set_window_size(542, 554)
    width_after = chrome_driver.find_element(By.CSS_SELECTOR, ".btn-success").value_of_css_property('width')
    assert width_before != width_after
    chrome_driver.quit()


def test_default_input_page_title():
    sleep(5)
    assert "Фильтр для гласных" in chrome_driver.title
    sleep(5)
    chrome_driver.quit()


def test_default_input_header():
   header = chrome_driver.find_element(By.XPATH, "//label[contains(text(),\'Введите текст:\')]").text
   assert header == "Введите текст:"
   chrome_driver.quit()


def test_input_field_has_default_text():
    sleep(5)
    assert chrome_driver.find_element("name", 'text_input').text == default_input_text
    chrome_driver.quit()


def test_default_input_with_leave_vowels_button():
    sleep(5)
    chrome_driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    test_output_vowels = chrome_driver.find_element("id", "text_output").text
    assert test_output_vowels == default_output_vowels
    chrome_driver.quit()


def test_default_values_with_highlight_result_button():
    sleep(5)
    chrome_driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    chrome_driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    text_output = chrome_driver.find_element("id", "text_output").text
    my_selection = pyperclip.copy(text_output)
    input_field = chrome_driver.find_element("name", 'text_input')
    system_selection = input_field.send_keys(text_output)
    assert my_selection == system_selection
    chrome_driver.quit()


def test_default_values_with_leave_vowels_whitespace_button():
    sleep(5)
    chrome_driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    test_output_vowels = chrome_driver.find_element("id", "text_output").text
    assert test_output_vowels == default_output_vowels_whitespace
    chrome_driver.quit()


def test_vowels_filter_leave_vowels_whitespace_symbols():
    sleep(5)
    chrome_driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()
    test_output_vowels = chrome_driver.find_element("id", "text_output").text
    assert test_output_vowels == default_output_vowels_whitespace_symbols
    chrome_driver.quit()



