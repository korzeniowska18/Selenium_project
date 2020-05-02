from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def test_registration():
    driver = webdriver.Chrome(ChromeDriverManager("80.0.3987.106").install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://centrumamis.pl/pl")
    driver.find_element_by_xpath("//span[text()='Zarejestruj się']").click()
    print("Sprawdzamy czy można się zarejestrować nie wprowadzając żadnych danych")
    driver.find_element_by_css_selector("#box_register > form > fieldset > div.innerbox.address-handler > div.bottombuttons > button").click()
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/p").get_attribute("textContent")
    alert = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/p").get_attribute("textContent")
    if len(alert) > 0:
        print("Alert o błedach podczas rejestracji pojawił się prawidłowo. Nie ma możliwości rejetracji bez wprowadzenia odpowiednich danych")
    else:
        print("Alert o błedach podczas rejestracji nie pojawił się. Bład formularza rejestracji.")
    driver.save_screenshot("screenshots/alert_screenshot.png")

    driver.quit()


