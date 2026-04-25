from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost:5000")
time.sleep(2)

# Enter name
driver.find_element(By.NAME, "name").send_keys("Devika")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)

text = driver.page_source

if "Hello Devika" in text:
    print("TEST PASSED")
else:
    print("TEST FAILED")

driver.quit()