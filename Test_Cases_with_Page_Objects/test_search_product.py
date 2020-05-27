from selenium import webdriver
from page_object_pattern.pages.amis_home_page import AmisHomePage
from page_object_pattern.pages.amis_result_page import AmisResultPage
from page_object_pattern.pages.amis_search_page import AmisSearchPage
from page_object_pattern.pages.amis_add_to_cart_page import AmisAddToCartPage
from page_object_pattern.pages.amis_alert_message_page import AmisAlertMessagePage



import pytest
from webdriver_manager.chrome import ChromeDriverManager

class TestAmisSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_amis_search(self, setup):
        self.driver.get("https://centrumamis.pl")
        home_page = AmisHomePage(self.driver)
        home_page.search_in_amis("waga")
        amis_search_result = AmisResultPage(self.driver)
        amis_search_result.open_first_product()
        amis_search_product = AmisSearchPage(self.driver)
        amis_search_product.search_product()
        add_product_to_cart = AmisAddToCartPage(self.driver)
        add_product_to_cart.add_to_cart()
        alert_message_appears = AmisAlertMessagePage(self.driver)
        alert_message_appears.alert_message_product_add_to_cart()

        print("Test case 'TestSearchProduct' completed")

