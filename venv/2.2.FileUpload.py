from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

browser.find_element(By.NAME, "firstname").send_keys('Хуй')
browser.find_element(By.NAME, "lastname").send_keys('Пизда')
browser.find_element(By.NAME, "email").send_keys('SADasdsd13@yabdex.com')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "2.2.FileUpload.txt"
file_path = os.path.join(current_dir, file_name)

browser.find_element(By.ID, "file").send_keys(file_path)

browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
time.sleep(11)