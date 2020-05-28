class AmisAlertMessagePage:

    def __init__(self, driver):
        self.driver = driver
        self.alert_message_product_add_to_cart_name = "p"

    def alert_message_product_add_to_cart(self):
        alert_message = self.driver.find_element_by_tag_name(self.alert_message_product_add_to_cart_name)
        if alert_message.is_displayed():
            print("Alert message that product added to cart displayed correctly")
            print("Alert message: " + alert_message.text)
        else:
            print("Alert message that product added to cart not displayed. This is mistake on the page")
            print(alert_message.get_attribute("textContent"))
