from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from Pages.autocompletePage import AutocompletePage
from Locators.locators import Locators


class AutocompleteTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:/Programming/QA/Projects/qa-py-formy-app-testing/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get(Locators.baseURL + 'autocomplete')

    # Sending data to the autocompleted field
    def test_01_autocomplete_dropdown_address(self):
        driver = self.driver
        autocomplete = AutocompletePage(driver)
        autocomplete.autocomplete_field(autocomplete.full_address_text)
        time.sleep(2)
        autocomplete.autocomplete_dropdown_click()
        time.sleep(1)

    # Verifying if the form field were autocompleted
    def test_02_autocompleted_fields(self):
        driver = self.driver
        autocompleted_fields = AutocompletePage(driver)

        fields_list = [
            driver.find_element_by_id(autocompleted_fields.input_autocomplete_id).get_attribute("value"),
            driver.find_element_by_id(autocompleted_fields.input_street_number_id).get_attribute("value"),
            driver.find_element_by_id(autocompleted_fields.input_route_id).get_attribute("value"),
            driver.find_element_by_id(autocompleted_fields.input_postal_code_id).get_attribute("value"),
            driver.find_element_by_id(autocompleted_fields.input_locality_id).get_attribute("value"),
            driver.find_element_by_id(autocompleted_fields.input_administrative_area_level_1_id).get_attribute("value"),
            driver.find_element_by_id(autocompleted_fields.input_country_id).get_attribute("value")
        ]

        for input_field in fields_list:
            assert len(input_field) > 0

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Programming/QA/Projects/qa-py-formy-app-testing/reports'))
