from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#these tests were done using PyCharm


def test_log_in_passed():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    #wait = WebDriverWait(driver, 10)
    driver.get("https://centrumamis.pl/")
    driver.find_element_by_xpath("//a[@class='login']").click()
    driver.find_element_by_id("mail_input_long").send_keys("tester@example.com")
    driver.find_element(By.ID, "pass_input_long").send_keys("12345678")
    driver.find_element(By.ID, "pass_input_long").send_keys(Keys.ENTER)
    assert driver.find_element(By.LINK_TEXT, "Wyloguj").is_displayed()
    print("Assertion confirmed that User logged successful.")
    print("Test Case TestLoginPassed completed.")
    driver.save_screenshot("screenshots/screenshot1.png")

def test_log_in_failed():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://centrumamis.pl/")
    driver.find_element_by_xpath("//a[@class='login']").click()
    driver.find_element_by_id("mail_input_long").send_keys("tester@example.com")
    driver.find_element(By.ID, "pass_input_long").send_keys("123456789")
    driver.find_element(By.ID, "pass_input_long").send_keys(Keys.ENTER)
    #assert driver.find_element(By.XPATH, "//div[@class='row']/p").text == "Niepoprawne dane logowania."
    assert "Niepoprawne dane logowania." in driver.find_element(By.XPATH, "//div[@class='row']/p").text
    print("Assertion confirmed that User could not login and login failed.")
    print("Appeared error about incorrect login details: Niepoprawne dane logowania.")
    print("Test Case TestLoginFailed completed.")
    driver.save_screenshot("screenshots/screenshot2.png")
