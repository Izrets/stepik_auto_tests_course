from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")
browser.find_element(By.XPATH, "//body/form/div/div/button").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
# _________________________________ ____________________
x = browser.find_element(By.ID, "input_value").text
result = math.log(abs(12*math.sin(int(x))))
# _____________________________________________________
browser.find_element(By.CLASS_NAME, "form-control").send_keys(result)
browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
time.sleep(10)
browser.close()