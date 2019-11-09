from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def sum(x, y):
    return str(int(x)+int(y))

try:
    link1="http://suninjuly.github.io/selects1.html"
    link2="http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link1)

    num1 = browser.find_element_by_id("num1")
    x = num1.text
    num2 = browser.find_element_by_id("num2")
    y = num2.text
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(sum(x, y))

    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()

