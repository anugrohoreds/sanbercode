import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class TestHealthcare(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Drivers/chromedriver/chromedriver.exe")
    
    def make_appointment(self):
        driver = self.driver
        driver.get("https://katalon-demo-cura.herokuapp.com")
        driver.maximize_window()
        self.assertIn("CURA Healthcare Service",driver.title)
        entry_btn = driver.find_element(By.ID,"btn-make-appointment")
        entry_btn.click()
        username = driver.find_element(By.NAME,"username")
        password = driver.find_element(By.NAME,"password")
        username.send_keys("JohnDoe")
        username.send_keys(Keys.RETURN)
        password.send_keys("ThisIsNotPassword")
        password.send_keys(Keys.RETURN)
        login_button = driver.find_element(By.ID,"btn-login")
        login_button.click()
        sel = Select(driver.find_element(By.ID,"facility"))
        sel.select_by_visible_text("Tokyo CURA Healthcare Center")
        ckbox = driver.find_element(By.XPATH("//input[@id='chk_hospotal_readmission']"))
        ckbox.click()
        date = driver.find_element(By.XPATH("//input[@id='txt_visit_date']"))
        date.send_keys("22/07/2023")
        txt = driver.find_element(By.NAME("comment"))
        txt.send_keys("Youll Never Walk Alone")
        book_btn = driver.find_element(By.ID,"btn-book-appointment")
        book_btn.click()

    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main()