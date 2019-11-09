from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("data")
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("data")
    email = browser.find_element_by_name("email")
    email.send_keys("data")
    element = browser.find_element_by_css_selector("input[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'data.txt')           # добавляем к этому пути имя файла
    element.send_keys(file_path)
    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()