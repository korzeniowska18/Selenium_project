
	
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager("80.0.3987.106").install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://centrumamis.pl/pl")
driver.find_element_by_xpath("//span[text()='Zarejestruj się']").click()
print("Checking registration with empty all required fields and checkbox")
driver.find_elements_by_id("input_mail").clear()
driver.find_elements_by_id("input_pass1").clear()
driver.find_elements_by_id("input_pass2").clear()
driver.find_elements_by_id("additional_1").clear()
driver.find_element_by_css_selector("#box_register > form > fieldset > div.innerbox.address-handler > div.bottombuttons > button > span").click()

alerts = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div/div/p")
alerts_names = [alert.get_attribute("textContent") for alert in alerts]

for alert_name in alerts_names:
    print("Alert text is: " + alert_name)

assert alert_name == "Formularz rejestracji zawiera błędy."

print("This means that registration without input required data is impossible and this is correct behaviour")

driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/button/span").click()

driver.quit()
