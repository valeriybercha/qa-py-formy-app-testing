from selenium import webdriver
import unittest
import HtmlTestRunner
from Locators.locators import Locators
from Pages.switchWindowsPage import SwitchWindowsPage


class SwitchWindowsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:/Programming/QA/Projects/qa-py-formy-app-testing/drivers/chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(Locators.baseURL + 'switch-window')

    # New tab test
    def test_01_switchWindow_newTab(self):
        driver = self.driver
        switch_windows = SwitchWindowsPage(driver)
        switch_windows.newTab_button_click()
        driver.switch_to.window(driver.window_handles[1])
        driver.get(Locators.baseURL)
        assert driver.find_element_by_xpath("//h1[contains(text(), 'Welcome to Formy')]")
        driver.switch_to.window(driver.window_handles[0])

    # Alert modal test
    def test_02_switchWindow_alert(self):
        driver = self.driver
        switch_windows = SwitchWindowsPage(driver)
        switch_windows.alert_button_click()
        alert_obj = driver.switch_to.alert
        alert_obj.accept()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Programming/QA/Projects/qa-py-formy-app-testing/reports'))
