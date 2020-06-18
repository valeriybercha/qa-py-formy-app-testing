from selenium import webdriver
import unittest
import HtmlTestRunner
from Locators.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
from Tests.datepicker import today_date


class ScrollTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:/Programming/QA/Projects/qa-py-formy-app-testing/drivers/chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(Locators.baseURL + 'scroll')

    # Scroll at the bottom of the page and input the data
    def test_01_scroll(self):
        driver = self.driver
        scroll_name = driver.find_element_by_id('name')
        scroll_date = driver.find_element_by_id('date')
        action = ActionChains(driver)
        action.move_to_element(scroll_name)
        scroll_name.send_keys('Valeriy')
        scroll_date.send_keys(today_date())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Programming/QA/Projects/qa-py-formy-app-testing/reports'))
