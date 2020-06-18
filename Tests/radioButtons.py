from selenium import webdriver
import unittest
import HtmlTestRunner
from Locators.locators import Locators
from Pages.radioButtonsPage import RadioButtonsPage


class RadioButtonsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:/Programming/QA/Projects/qa-py-formy-app-testing/drivers/chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(Locators.baseURL + 'radiobutton')

    # Verifying radio button 1
    def test_01_radio_button_one(self):
        driver = self.driver
        radio_buttons = RadioButtonsPage(driver)
        radio_buttons.radio_button_one_click()
        assert driver.find_element_by_xpath(Locators.input_radio_one_xpath).is_selected()

    # Verifying radio button 2
    def test_02_radio_button_two(self):
        driver = self.driver
        radio_buttons = RadioButtonsPage(driver)
        radio_buttons.radio_button_two_click()
        assert driver.find_element_by_xpath(Locators.input_radio_two_xpath).is_selected()

    # Verifying radio button 3
    def test_03_radio_button_three(self):
        driver = self.driver
        radio_buttons = RadioButtonsPage(driver)
        radio_buttons.radio_button_three_click()
        assert not driver.find_element_by_xpath(Locators.input_radio_one_xpath).is_selected()
        assert not driver.find_element_by_xpath(Locators.input_radio_two_xpath).is_selected()
        assert driver.find_element_by_xpath(Locators.input_radio_three_xpath).is_selected()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Programming/QA/Projects/qa-py-formy-app-testing/reports'))
