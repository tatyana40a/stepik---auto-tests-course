from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio:", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots radio:", robots_checked)
    assert robots_checked is None, "Robots radio is selected by default"

    submit = browser.find_element_by_css_selector("button.btn")
    submit_disabled = submit.get_attribute("disabled")
    print("submit button is disabled by default:", submit_disabled)
    assert submit_disabled is None, "Submit button is disabled by default"

finally:
    time.sleep(10)
    browser.quit()