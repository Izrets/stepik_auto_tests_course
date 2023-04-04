import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/selects2.html")
numb1 = browser.find_element(By.ID, "num1").text
numb2 = browser.find_element(By.ID, "num2").text

answer = sum([int(numb2), int(numb1)])
print(answer)
time.sleep(2)
Select(browser.find_element(By.CSS_SELECTOR, "#dropdown")).select_by_value(str(answer))
# time.sleep(2)
# select.select_by_value(answer)
# time.sleep(2)
browser.find_element(By.CLASS_NAME, "btn.btn-default").click()
time.sleep(10)