from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# 🔹 Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 🔥 CONNECT TO SELENIUM SERVER (inside container)
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=options
)

# 🔹 Open your Flask app (running on host)
driver.get("http://host.docker.internal:5001")

time.sleep(3)

# 🔹 Perform test
driver.find_element(By.NAME, "name").send_keys("Devika")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)

text = driver.page_source

if "Hello Devika" in text:
    print("TEST PASSED")
else:
    print("TEST FAILED")

driver.quit()