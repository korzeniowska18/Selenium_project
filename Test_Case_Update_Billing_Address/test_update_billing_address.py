from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def test_billing_address_update():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://centrumamis.pl/")
    driver.find_element_by_xpath("//a[@class='login']").click()
    driver.find_element_by_id("mail_input_long").send_keys("tester@example.com")
    driver.find_element(By.ID, "pass_input_long").send_keys("12345678")
    driver.find_element(By.ID, "pass_input_long").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, "//a[@class='myaccount']/span").click()
    #driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/a[3]/span").click()
    driver.find_element(By.XPATH, "//a[@class='editaddresses btn spanhover']/span").click()
    driver.find_element(By.XPATH, "//a[@class='edit btn spanhover']/span").click()
    driver.find_element(By.ID, "input_phone").clear()
    driver.find_element(By.ID, "input_phone").send_keys("605234123")
    driver.find_element(By.ID, "input_other_address").clear()
    driver.find_element(By.ID, "input_other_address").send_keys("Marzeń 28")
    driver.find_element(By.ID, "input_zip").clear()
    driver.find_element(By.ID, "input_zip").send_keys("00-002")
    driver.find_element(By.ID, "input_city").clear()
    driver.find_element(By.ID, "input_city").send_keys("Warszawa")
    driver.find_element(By.ID, "input_country").send_keys("Polska")
    driver.find_element(By.NAME, "button2").click()
    assert "Adres został zapisany." in driver.find_element(By.XPATH, "//div[@class='row']/p").text
    print("Assertion confirmed that Billing Address for Account updated successfully.")
    print("Appeared error about update: Adres został zapisany.")
    print("Test Case TestBillingAddressUpdate completed.")
    driver.save_screenshot("screenshots/screenshot6.png")
