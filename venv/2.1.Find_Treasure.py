from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    x_element = browser.find_element(By.CSS_SELECTOR, "img, valuex").get_attribute("valuex")
    x = x_element
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "#robotcheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()

finally:
    time.sleep(7)
    browser.quit()
