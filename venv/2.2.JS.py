import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
x = browser.find_element(By.ID, "input_value").text
browser.find_element(By.CLASS_NAME, "form-control").send_keys((str(math.log(abs(12 * math.sin(int(x)))))))
browser.execute_script("window.scrollBy(0, 300);")
browser.find_element(By.ID, "robotCheckbox").click()
browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").submit()
time.sleep(10)



