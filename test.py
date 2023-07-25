from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Drivers/chromedriver/chromedriver.exe")
driver.get("https://www.google.com")
assert "Google" in driver.title
elem = driver.find_element(By.NAME,"q")
elem.clear()
elem.send_keys("Tazkiyah Nurlaili Citra Dewi")
elem.send_keys(Keys.RETURN)
assert "No results ." not in driver.page_source
driver.close()

