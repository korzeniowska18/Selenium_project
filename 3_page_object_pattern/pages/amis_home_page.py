class AmisHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.search_input_name = 'search'
        self.search_button_xpath = '/html/body/div[1]/header/div[2]/div[3]/form/div[1]/div[3]/button'

    def search_in_amis(self, text):
        self.driver.find_element_by_name(self.search_input_name).send_keys(text)
        self.driver.find_element_by_xpath(self.search_button_xpath).click()
