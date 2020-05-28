import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random


class TestUpdateData(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://centrumamis.pl/")
        self.driver.maximize_window()
        sleep(2)

    def tearDown(self):
        self.driver.quit()

    def testUpdateBillingAddress(self):
        driver = self.driver
        open_login_page = WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.XPATH, "//a[@class='login']")))
        open_login_page.click()
        username_input = driver.find_element_by_id("mail_input_long")
        username_input.send_keys("tester@example.com")
        password_input = driver.find_element(By.ID, "pass_input_long")
        password_input.send_keys("12345678")
        password_input.send_keys(Keys.ENTER)
        select_my_account = driver.find_element(By.XPATH, "//a[@class='myaccount']/span")
        select_my_account.click()
        open_edit_address = driver.find_element(By.XPATH, "//a[@class='editaddresses btn spanhover']/span")
        open_edit_address.click()
        edit_button = driver.find_element(By.XPATH, "//a[@class='edit btn spanhover']/span")
        edit_button.click()
        first_name_field = driver.find_element(By.ID, "input_name")
        first_name_field.clear()
        first_name_field.send_keys("Natali")
        last_name_field = driver.find_element(By.ID, "input_surname")
        last_name_field.clear()
        last_name_field.send_keys("Testerka")
        company_name_field = driver.find_element(By.ID, "input_coname")
        company_name_field.clear()
        company_name_field.send_keys("Tester Automatyczny")
        phone_number_field = driver.find_element(By.ID, "input_phone")
        phone_number_field.clear()
        input_phone_number = str(random.randint(0, 1000)) + "605234123"
        phone_number_field.send_keys(input_phone_number)
        address_field = driver.find_element(By.ID, "input_other_address")
        address_field.clear()
        input_address = str(random.randint(0, 1000)) + "Marzeń 29"
        address_field.send_keys(input_address)
        zip_field = driver.find_element(By.ID, "input_zip")
        zip_field.clear()
        zip_field.send_keys("00-002")
        city_field = driver.find_element(By.ID, "input_city")
        city_field.clear()
        city_field.send_keys("Warszawa")
        country_field = driver.find_element(By.ID, "input_country")
        country_field.send_keys("Polska")
        save_button = driver.find_element(By.NAME, "button2")
        save_button.click()
        assert "Adres został zapisany." in driver.find_element(By.XPATH, "//div[@class='row']/p").text
        print("Assertion confirmed that Billing Address for Account updated successfully.")
        print("Appeared error about update: Adres został zapisany.")
        print("Test Case TestUpdateBillingAddress completed.")



if __name__ == '__main__':
    unittest.main(verbosity=2)
