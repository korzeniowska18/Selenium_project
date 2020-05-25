import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random


class TestLoginAccount(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://centrumamis.pl/")
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()


    def testLoginPassed(self):
        driver = self.driver
        open_login_page = WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.XPATH, "//a[@class='login']")))
        open_login_page.click()
        username_input = driver.find_element_by_id("mail_input_long")
        username_input.send_keys("tester@example.com")
        password_input = driver.find_element(By.ID, "pass_input_long")
        password_input.send_keys("12345678")
        password_input.send_keys(Keys.ENTER)
        confirmation_about_login = driver.find_element(By.XPATH, "//span[text()='Wyloguj']")
        print(f"After passed login to Account appears tab: {confirmation_about_login.text}")
        greeting_for_logged_account = driver.find_element(By.XPATH, '//p[text()="Witaj "]')
        print(f"After passed login to Account appears greeting: {greeting_for_logged_account.text}")
        assert greeting_for_logged_account.text=="Witaj TesterAutomatyczny"
        print("Assertion confirmed that User logged successful.")
        print("Test Case №1 'TestLoginPassed' completed.")

    def testLoginFailedWrongEmail(self):
        driver = self.driver
        open_login_page = WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.XPATH, "//a[@class='login']")))
        open_login_page.click()
        wrong_username_input = driver.find_element_by_id("mail_input_long")
        wrong_username_input.send_keys("tester.example.com")
        password_input = driver.find_element(By.ID, "pass_input_long")
        password_input.send_keys("12345678")
        password_input.send_keys(Keys.ENTER)
        error_message = driver.find_element(By.XPATH, "//p[text()='Niepoprawne dane logowania.']")
        print(f"Appears error message about incorrect login details: {error_message.text}")
        assert error_message.text=="Niepoprawne dane logowania."
        print("Assertion confirmed that User not logged if used email without '@', login failed.")
        print("Test Case №2 'testLoginFailedWrongEmail' completed.")

    def testLoginFailedNotRegisteredEmail(self):
        driver = self.driver
        open_login_page = WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.XPATH, "//a[@class='login']")))
        open_login_page.click()
        wrong_email_input = str(random.randint(0, 1000)) + "tester1@example.com"
        wrong_username_input = driver.find_element_by_id("mail_input_long")
        wrong_username_input.send_keys(wrong_email_input)
        password_input = driver.find_element(By.ID, "pass_input_long")
        password_input.send_keys("12345678")
        password_input.send_keys(Keys.ENTER)
        error_message = driver.find_element(By.XPATH, "//p[text()='Niepoprawne dane logowania.']")
        print(f"Appears error message about incorrect login details: {error_message.text}")
        assert error_message.text=="Niepoprawne dane logowania."
        print("Assertion confirmed that User not logged if used not registered email, login failed.")
        print("Test Case №3 'testLoginFailedNotRegisteredEmail' completed.")



if __name__ == '__main__':
    unittest.main(verbosity=2)
