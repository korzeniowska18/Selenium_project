class AmisHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.search_input_name = 'search'
        self.search_button_xpath = '//div[@class="search__input-area-item"]'

    def search_in_amis(self, text):
        self.driver.find_element_by_name(self.search_input_name).send_keys(text)
        self.driver.find_element_by_xpath(self.search_button_xpath).click()
