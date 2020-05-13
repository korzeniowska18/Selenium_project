from selenium import webdriver
from page_object_pattern.pages.amis_home_page import AmisHomePage
from page_object_pattern.pages.amis_result_page import AmisResultPage



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


