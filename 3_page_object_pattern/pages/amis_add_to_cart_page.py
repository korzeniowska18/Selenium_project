class AmisAddToCartPage:

    def __init__(self, driver):
        self.driver = driver
        self.add_product_to_cart_xpath = "//button[@class='addtobasket btn btn-red']"

    def add_to_cart(self):
        self.driver.find_element_by_xpath(self.add_product_to_cart_xpath).click()
        print("Product added to cart successful")
