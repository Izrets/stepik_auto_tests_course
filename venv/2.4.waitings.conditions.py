import math
import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")


button = browser.find_element(By.ID, "book")
WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
button.click()
x = browser.find_element(By.ID, "input_value")
x_element = x.text
print(x_element)
znach = math.log(abs(12*math.sin(int(x_element))))
browser.find_element(By.ID, "answer").send_keys(znach)
browser.find_element(By.ID, "solve").click()
time.sleep(10)