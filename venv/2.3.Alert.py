from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")
browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
confirm = browser.switch_to.alert
confirm.accept()
# _____________________________________________________
x = browser.find_element(By.ID, "input_value").text
result = math.log(abs(12*math.sin(int(x))))
# _____________________________________________________
browser.find_element(By.CLASS_NAME, "form-control").send_keys(result)
browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
time.sleep(10)
browser.close()