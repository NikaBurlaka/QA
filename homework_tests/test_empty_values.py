from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import pyperclip

s = Service("/usr/local/bin/chromedriver")
chrome_driver = webdriver.Chrome(service=s)
chrome_driver.get("https://rioran.github.io/ru_vowels_filter/main.html")
text_input = chrome_driver.find_element("id", 'text_input')
text_input.clear()


def test_empty_values_with_leave_vowels_button():
    sleep(5)
    chrome_driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    text_output = chrome_driver.find_element("id", "text_output").text
    assert text_output == ''


def test_empty_values_with_leave_vowels_whitespace_button():
    sleep(5)
    chrome_driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    text_output = chrome_driver.find_element("id", "text_output").text
    assert text_output == ''
    chrome_driver.quit()


def test_empty_values_with_leave_vowels_whitespace_symbols_button():
    sleep(5)
    chrome_driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()
    text_output = chrome_driver.find_element("id", "text_output").text
    assert text_output == ''
    chrome_driver.quit()


def test_empty_values_with_highlight_result_button():
    sleep(5)
    chrome_driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    text_output = chrome_driver.find_element("id", "text_output").text
    my_selection = pyperclip.copy(text_output)
    input_field = chrome_driver.find_element("name", 'text_input')
    system_selection = input_field.send_keys(text_output)
    assert my_selection == system_selection


def test_empty_values_with_leave_vowels_and_highlight_result_button():
    sleep(5)
    chrome_driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    chrome_driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    test_output_vowels = chrome_driver.find_element("id", "text_output").text
    assert test_output_vowels == ''
    chrome_driver.quit()
