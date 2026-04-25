from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 🔹 Configure headless Chrome
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# 🔥 IMPORTANT FIX
driver.get("http://host.docker.internal:5001")

time.sleep(3)

# 🔹 Enter name
driver.find_element(By.NAME, "name").send_keys("Devika")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)

text = driver.page_source

if "Hello Devika" in text:
    print("TEST PASSED")
else:
    print("TEST FAILED")

driver.quit()