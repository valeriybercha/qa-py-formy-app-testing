import unittest
import HtmlTestRunner
from Pages.checkboxesPage import CheckboxesPage
from Locators.locators import Locators
from selenium import webdriver


class CheckboxesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:/Programming/QA/Projects/qa-py-formy-app-testing/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get(Locators.baseURL + 'checkbox')

    # Clicking all the checkboxes
    def test_01_click_checkboxes(self):
        driver = self.driver
        click_checkboxes = CheckboxesPage(driver)
        click_checkboxes.checkbox_one_click()
        click_checkboxes.checkbox_two_click()
        click_checkboxes.checkbox_three_click()

    # Verifying if the checkbox is selected
    def test_02_check_checkbox_attribute(self):
        driver = self.driver
        checkbox_attribute = CheckboxesPage(driver)
        checkbox_attribute.checkbox_one_is_selected()
        checkbox_attribute.checkbox_two_is_selected()
        checkbox_attribute.checkbox_three_is_selected()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Programming/QA/Projects/qa-py-formy-app-testing/reports'))
