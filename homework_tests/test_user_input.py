from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyperclip
from selenium.webdriver.common.by import By
from time import sleep

s = Service("/usr/local/bin/chromedriver")
chrome_driver = webdriver.Chrome(service=s)
chrome_driver.get("https://rioran.github.io/ru_vowels_filter/main.html")

my_input_text = 'дальше, Английские. буквы!: aeoy1'

text_input = chrome_driver.find_element("id", 'text_input')
text_input.clear()
input_field = chrome_driver.find_element("name", 'text_input')
input_field.send_keys(my_input_text)


def test_user_input_with_leave_vowels_button():
    sleep(5)
    chrome_driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    test_output_vowels = chrome_driver.find_element("id", "text_output").text
    assert test_output_vowels == 'аеаииеуы'
    sleep(4)
    chrome_driver.quit()


def test_user_input_with_leave_vowels_whitespace_button():
    sleep(5)
    chrome_driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    test_output_vowels = chrome_driver.find_element("id", "text_output").text
    assert test_output_vowels == 'ае аиие уы'
    sleep(4)
    chrome_driver.quit()


def test_user_input_with_leave_vowels_whitespace_button_symbols_button():
    sleep(5)
    chrome_driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()
    test_output_vowels = chrome_driver.find_element("id", "text_output").text
    assert test_output_vowels == 'ае, аиие. уы!'
    chrome_driver.quit()

    
def test_user_input_with_leave_vowels_and_highlight_text_button():
    sleep(5)
    chrome_driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    chrome_driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    text_output = chrome_driver.find_element("id", "text_output").text
    my_selection = pyperclip.copy(text_output)
    input_field = chrome_driver.find_element("name", 'text_input')
    system_selection = input_field.send_keys(text_output)
    assert my_selection == system_selection
    chrome_driver.quit()
