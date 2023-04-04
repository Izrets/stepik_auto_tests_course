from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://magento.softwaretestingboard.com')

browser.find_element(By.CLASS_NAME, "action.more.button").click()
time.sleep(0.5)
browser.find_element(By.XPATH, "//body/div/main//div[3]/div/div[3]/ol/li[3]/div/div/strong/a").click()
time.sleep(0.5)
browser.find_element(By.CSS_SELECTOR, "#option-label-size-143-item-171").click()
time.sleep(0.5)
browser.find_element(By.CSS_SELECTOR, "#option-label-color-93-item-49").click()
time.sleep(0.5)
browser.find_element(By.CSS_SELECTOR, "#qty").clear()
browser.find_element(By.CSS_SELECTOR, "#qty").send_keys("3")
time.sleep(0.5)
browser.find_element(By.CSS_SELECTOR, "#product-addtocart-button").click()
time.sleep(5)

get_source = browser.page_source
time.sleep(5)
search_text = "You added Fiona"
# print(search_text in get_source)
print(search_text in get_source)



