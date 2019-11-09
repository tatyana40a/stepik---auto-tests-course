from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element_by_id("treasure")
    x = chest.get_attribute("valuex")
    y = calc(x)

    field = browser.find_element_by_id("answer")
    field.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_radio.click()

    submit = browser.find_element_by_css_selector('button.btn')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()