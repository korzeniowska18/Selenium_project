class AmisSearchPage:

    def __init__(self, driver):
         self.driver = driver
         self.search_product_xpath = "//span[@class='productname']"

    def search_product(self):
        print("Product name: " + self.driver.find_element_by_xpath(self.search_product_xpath).get_attribute("textContent"))
