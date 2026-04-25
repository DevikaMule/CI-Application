from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

driver.get("http://localhost:5000")

time.sleep(3)

driver.find_element(By.NAME, "name").send_keys("Devika")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)

if "Hello Devika" in driver.page_source:
    print("TEST PASSED")
else:
    print("TEST FAILED")

driver.quit()