from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    element_x = browser.find_element_by_id("input_value")
    x = element_x.text
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(x))
    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

