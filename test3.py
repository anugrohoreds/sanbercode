import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class GoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Drivers/chromedriver/chromedriver.exe")
    
    def test_search_test(self):
        driver = self.driver
        driver.get("https://www.yahoo.com")
        elem = driver.find_element(By.NAME,"p")
        elem.clear()
        elem.send_keys("Liverpool FC")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()