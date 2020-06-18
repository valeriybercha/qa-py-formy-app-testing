from selenium import webdriver
import unittest
import HtmlTestRunner
from Pages.modalPage import ModalPage
from Locators.locators import Locators


class ModalTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:/Programming/QA/Projects/qa-py-formy-app-testing/drivers/chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(Locators.baseURL + 'modal')

    # Click the modal button and check for the modal window header
    def test_01_modal_form(self):
        driver = self.driver
        modal = ModalPage(driver)
        modal.modal_button_click()
        assert driver.find_element_by_xpath("//h5[contains(text(), 'Modal title')]")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Programming/QA/Projects/qa-py-formy-app-testing/reports'))
