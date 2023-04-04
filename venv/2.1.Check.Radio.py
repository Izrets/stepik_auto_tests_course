from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/math.html')

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    (browser.find_element(By.CLASS_NAME, "form-control")).send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "#robotcheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()

finally:
    time.sleep(7)
    browser.quit()
