import unittest
import HtmlTestRunner
from Pages.buttonsPage import ButtonsPage
from Locators.locators import Locators
from selenium import webdriver


class ButtonsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:/Programming/QA/Projects/qa-py-formy-app-testing/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get(Locators.baseURL + 'buttons')

    # Testing the first row of buttons
    def test_01_row_buttons_click(self):
        driver = self.driver
        buttons_first_row = ButtonsPage(driver)
        buttons_first_row.first_row_button_primary()
        buttons_first_row.first_row_button_success()
        buttons_first_row.first_row_button_info()
        buttons_first_row.first_row_button_warning()
        buttons_first_row.first_row_button_danger()
        buttons_first_row.first_row_button_link()

    # Testing the second row of buttons
    def test_02_row_buttons_click(self):
        driver = self.driver
        buttons_second_row = ButtonsPage(driver)
        buttons_second_row.second_row_button_left()
        buttons_second_row.second_row_button_middle()
        buttons_second_row.second_row_button_right()

    # Testing the third row of buttons
    def test_03_row_buttons_click(self):
        driver = self.driver
        buttons_third_row = ButtonsPage(driver)
        buttons_third_row.third_row_button_one()
        buttons_third_row.third_row_button_two()
        buttons_third_row.third_row_button_dropdown()
        buttons_third_row.third_row_button_dropdown_one()
        buttons_third_row.third_row_button_dropdown()
        buttons_third_row.third_row_button_dropdown_two()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Programming/QA/Projects/qa-py-formy-app-testing/reports'))
