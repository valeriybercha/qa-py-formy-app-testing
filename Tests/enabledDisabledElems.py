from selenium import webdriver
import unittest
import HtmlTestRunner
from Pages.enabledDisabledElemsPage import EnabledDisabledElemsPage
from Locators.locators import Locators


class EnabledDisabledElemsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:/Programming/QA/Projects/qa-py-formy-app-testing/drivers/chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(Locators.baseURL + 'enabled')

    def test_01_disabled_input_pass(self):
        driver = self.driver
        disabled_input = EnabledDisabledElemsPage(driver)
        if not disabled_input.disabled_input_pass():
            pass

    def test_02_enabled_input_click(self):
        driver = self.driver
        enabled_input = EnabledDisabledElemsPage(driver)
        if enabled_input.enabled_input_pass():
            enabled_input.enabled_input_pass().send_keys(Locators.full_address_text)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Programming/QA/Projects/qa-py-formy-app-testing/reports'))
