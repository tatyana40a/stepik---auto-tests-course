from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('input.first[required]')
    input1.send_keys('data')
    input2 = browser.find_element_by_css_selector('input.second[required]')
    input2.send_keys('data')
    input3 = browser.find_element_by_css_selector('input.third[required]')
    input3.send_keys('data')
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name('h1')
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()