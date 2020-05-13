class AmisResultPage:

    def __init__(self, driver):
         self.driver = driver
         self.search_results_xpath = "//a[@class='prodname f-row']"

    def open_first_product(self):
        self.driver.find_element_by_xpath(self.search_results_xpath).click()
