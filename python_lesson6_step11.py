from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    required_fields = browser.find_elements_by_css_selector('input[required]')
    for element in required_fields:
        element.send_keys('data')

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name('h1')
    welcome_text = welcome_text_elt.text

    assert len(required_fields) == 3
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()