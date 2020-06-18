from selenium import webdriver
import unittest
import HtmlTestRunner
from Locators.locators import Locators
from Pages.completeWebFormPage import CompleteWebFormPage
import time


class CompleteWebFormTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:/Programming/QA/Projects/qa-py-formy-app-testing/drivers/chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(Locators.baseURL + 'form')

    # First name input test
    def test_01_firstName(self):
        driver = self.driver
        form = CompleteWebFormPage(driver)
        form.firstName_input('Valeriy')
        attr = driver.find_element_by_id(Locators.input_webForm_firstName_id).get_attribute("value")
        assert len(attr) > 0

    # First name input test
    def test_02_lastName(self):
        driver = self.driver
        form = CompleteWebFormPage(driver)
        form.lastName_input('Valeriy')
        attr = driver.find_element_by_id(Locators.input_webForm_lastName_id).get_attribute("value")
        assert len(attr) > 0

    # Job title input test
    def test_03_job(self):
        driver = self.driver
        form = CompleteWebFormPage(driver)
        form.job_input('Software tester')
        attr = driver.find_element_by_id(Locators.input_webForm_job_id).get_attribute("value")
        assert len(attr) > 0

    # Radio buttons test
    def test_04_radioButtons(self):
        driver = self.driver
        form = CompleteWebFormPage(driver)
        form.radio_button_1_click()
        form.radio_button_2_click()
        form.radio_button_3_click()
        assert driver.find_element_by_id(Locators.input_webForm_radioButton3_id).is_selected()
        assert not driver.find_element_by_id(Locators.input_webForm_radioButton1_id).is_selected()
        assert not driver.find_element_by_id(Locators.input_webForm_radioButton2_id).is_selected()

    # Checkboxes buttons test
    def test_05_checkboxes(self):
        driver = self.driver
        form = CompleteWebFormPage(driver)
        form.radio_checkbox_1_click()
        form.radio_checkbox_2_click()
        form.radio_checkbox_3_click()
        assert driver.find_element_by_id(Locators.input_webForm_checkbox1_id).is_selected()
        assert driver.find_element_by_id(Locators.input_webForm_checkbox2_id).is_selected()
        assert driver.find_element_by_id(Locators.input_webForm_checkbox3_id).is_selected()

    # Dropdown menu selection test
    def test_06_dropdownMenu_selection(self):
        driver = self.driver
        form = CompleteWebFormPage(driver)
        form.dropdown_menu_click()
        form.dropdown_option_select_click()
        assert driver.find_element_by_xpath(Locators.option_webForm_selectOption_xpath).is_selected()
        form.dropdown_option_0_1_click()
        assert driver.find_element_by_xpath(Locators.option_webForm_0_1_xpath).is_selected()
        form.dropdown_option_2_4_click()
        assert driver.find_element_by_xpath(Locators.option_webForm_2_4_xpath).is_selected()
        form.dropdown_option_5_9_click()
        assert driver.find_element_by_xpath(Locators.option_webForm_5_9_xpath).is_selected()
        form.dropdown_option_10_plus_click()
        assert driver.find_element_by_xpath(Locators.option_webForm_10_plus_xpath).is_selected()

    # Datepicker selection test
    def test_07_datepicker_input(self):
        driver = self.driver
        form = CompleteWebFormPage(driver)
        form.datepicker_input('06/17/2020')
        form.datepicker_click()

    # Submit and redirect test
    def test_08_submit_redirect(self):
        driver = self.driver
        form = CompleteWebFormPage(driver)
        form.submit_button_click()
        time.sleep(2)
        assert driver.find_element_by_xpath("//h1[contains(text(), 'Thanks for submitting your form')]")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Programming/QA/Projects/qa-py-formy-app-testing/reports'))
