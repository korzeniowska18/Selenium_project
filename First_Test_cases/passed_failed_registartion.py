from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random



def test_create_account_failed():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://centrumamis.pl/pl/reg")
    driver.maximize_window()
    driver.find_element(By.ID, "input_mail").send_keys("tester@example.com")
    driver.find_element(By.ID, "input_pass1").send_keys("1234567")
    driver.find_element(By.ID, "input_pass2").send_keys("1234567")
    driver.find_element(By.ID, "input_pass2").send_keys(Keys.ENTER)
    alert_message = "Formularz rejestracji zawiera błędy."
    assert alert_message in driver.find_element(By.XPATH, "//div[@class='row']/p").text
    alert_message_about_registartion = "W sklepie istnieje już wpis tester@example.com"
    assert alert_message_about_registartion in driver.find_element(By.XPATH, "//div[@class='input_error']/li").text
    print("Assertion confirmed that User not registered. Appeared alert about mistake.")
    print("Alert message: " + alert_message_about_registartion)
    print("Test Case TestCreateAccountFailed completed.")

def test_create_account_passed():
    email = str(random.randint(0, 1000)) + "tester@example.com"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://centrumamis.pl/pl/reg")
    driver.maximize_window()
    driver.find_element(By.ID, "input_mail").send_keys(email)
    driver.find_element(By.ID, "input_pass1").send_keys("1234567")
    driver.find_element(By.ID, "input_pass2").send_keys("1234567")
    driver.find_element(By.ID, "input_pass2").send_keys(Keys.ENTER)
    alert_message_successful_registration = "Dziękujemy za założenie konta."
    assert alert_message_successful_registration in driver.find_element(By.XPATH, "//div[@class='row']/p").text
    assert driver.find_element(By.LINK_TEXT, "Wyloguj").is_displayed()
    print("Assertion confirmed that User registered successful.")
    print("Alert message: " + alert_message_successful_registration)
    print("Test Case TestCreateAccountPassed completed.")
