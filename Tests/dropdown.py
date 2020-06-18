from selenium import webdriver
import unittest
import HtmlTestRunner
from Pages.dropdownPage import DropdownPage
from Locators.locators import Locators
import time


class DropdownTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:/Programming/QA/Projects/qa-py-formy-app-testing/drivers/chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(Locators.baseURL + 'dropdown')

    # Autocomplete dropdown buttons click
    def test_01_autocomplete_dropdown_click(self):
        driver = self.driver
        droppdown_elements = DropdownPage(driver)
        droppdown_elements.dropdown_button_click()
        time.sleep(1)
        droppdown_elements.autocomplete_dropdown_button_click()
        time.sleep(1)
        assert driver.find_element_by_xpath("//h1[contains(text(),'Autocomplete')]")
        driver.back()
        time.sleep(1)

    # Buttons dropdown buttons click
    def test_02_buttons_dropdown_click(self):
        driver = self.driver
        droppdown_elements = DropdownPage(driver)
        droppdown_elements.dropdown_button_click()
        time.sleep(1)
        droppdown_elements.buttons_dropdown_button_click()
        time.sleep(1)
        assert driver.find_element_by_xpath("//button[contains(text(),'Primary')]")
        driver.back()
        time.sleep(1)

    # Checkbox dropdown buttons click
    def test_03_checkbox_dropdown_click(self):
        driver = self.driver
        droppdown_elements = DropdownPage(driver)
        droppdown_elements.dropdown_button_click()
        time.sleep(1)
        droppdown_elements.checkbox_dropdown_button_click()
        time.sleep(1)
        assert driver.find_element_by_xpath("//h1[contains(text(),'Checkboxes')]")
        driver.back()
        time.sleep(1)

    # Datepicker dropdown buttons click
    def test_04_datepicker_dropdown_click(self):
        driver = self.driver
        droppdown_elements = DropdownPage(driver)
        droppdown_elements.dropdown_button_click()
        time.sleep(1)
        droppdown_elements.datepicker_dropdown_button_click()
        time.sleep(1)
        assert driver.find_element_by_xpath("//h1[contains(text(),'Datepicker')]")
        driver.back()
        time.sleep(1)

    # Drag and drop dropdown buttons click
    def test_05_dragDrop_dropdown_click(self):
        driver = self.driver
        droppdown_elements = DropdownPage(driver)
        droppdown_elements.dropdown_button_click()
        time.sleep(1)
        droppdown_elements.draganddrop_dropdown_button_click()
        time.sleep(1)
        assert driver.find_element_by_xpath("//h1[contains(text(),'Drag the image into the box')]")
        driver.back()
        time.sleep(1)

    # Drropdown dropdown buttons click
    def test_06_dropdown_dropdown_click(self):
        driver = self.driver
        droppdown_elements = DropdownPage(driver)
        droppdown_elements.dropdown_button_click()
        time.sleep(1)
        droppdown_elements.dropdown_dropdown_button_click()
        time.sleep(1)
        assert driver.find_element_by_xpath("//h1[contains(text(),'Dropdown')]")
        time.sleep(1)

    # Enable and disable elements dropdown buttons click
    def test_07_enableDisableElements_dropdown_click(self):
        driver = self.driver
        droppdown_elements = DropdownPage(driver)
        droppdown_elements.dropdown_button_click()
        time.sleep(1)
        droppdown_elements.enabledisableelems_dropdown_button_click()
        time.sleep(1)
        assert driver.find_element_by_xpath("//h1[contains(text(),'Enabled and Disabled elements')]")
        driver.back()
        time.sleep(1)

    # File upload dropdown buttons click
    def test_08_fileUpload_dropdown_click(self):
        driver = self.driver
        droppdown_elements = DropdownPage(driver)
        droppdown_elements.dropdown_button_click()
        time.sleep(1)
        droppdown_elements.fileupload_dropdown_button_click()
        time.sleep(1)
        assert driver.find_element_by_xpath("//h1[contains(text(),'File upload')]")
        driver.back()
        time.sleep(1)

    # File download dropdown buttons click
    def test_09_fileDownload_dropdown_click(self):
        driver = self.driver
        droppdown_elements = DropdownPage(driver)
        droppdown_elements.dropdown_button_click()
        time.sleep(1)
        droppdown_elements.filedownload_dropdown_button_click()
        time.sleep(1)
        assert driver.find_element_by_xpath("//p[contains(text(),'You may have mistyped the address or the page may')]")
        driver.back()
        time.sleep(1)

    # Keyboard and mouse input dropdown buttons click
    def test_10_keyboardMouseInput_dropdown_click(self):
        driver = self.driver
        droppdown_elements = DropdownPage(driver)
        droppdown_elements.dropdown_button_click()
        time.sleep(1)
        droppdown_elements.keymousepress_dropdown_button_click()
        time.sleep(1)
        assert driver.find_element_by_xpath("//h1[contains(text(),'Keyboard and Mouse Input')]")
        driver.back()
        time.sleep(1)

    # Modal dropdown buttons click
    def test_11_modal_dropdown_click(self):
        driver = self.driver
        droppdown_elements = DropdownPage(driver)
        droppdown_elements.dropdown_button_click()
        time.sleep(1)
        droppdown_elements.modal_dropdown_button_click()
        time.sleep(1)
        assert driver.find_element_by_xpath("//h1[contains(text(),'Modal')]")
        driver.back()
        time.sleep(1)

    # Page scroll dropdown buttons click
    def test_12_pageScroll_dropdown_click(self):
        driver = self.driver
        droppdown_elements = DropdownPage(driver)
        droppdown_elements.dropdown_button_click()
        time.sleep(1)
        droppdown_elements.pagescroll_dropdown_button_click()
        time.sleep(1)
        assert driver.find_element_by_xpath("//h1[contains(text(),'Large page content')]")
        driver.back()
        time.sleep(1)

    # Radio buttons dropdown buttons click
    def test_13_radioButtons_dropdown_click(self):
        driver = self.driver
        droppdown_elements = DropdownPage(driver)
        droppdown_elements.dropdown_button_click()
        time.sleep(1)
        droppdown_elements.radiobutton_dropdown_button_click()
        time.sleep(1)
        assert driver.find_element_by_xpath("//h1[contains(text(),'Radio buttons')]")
        driver.back()
        time.sleep(1)

    # Switch window dropdown buttons click
    def test_14_switchWindow_dropdown_click(self):
        driver = self.driver
        droppdown_elements = DropdownPage(driver)
        droppdown_elements.dropdown_button_click()
        time.sleep(1)
        droppdown_elements.switchwindow_dropdown_button_click()
        time.sleep(1)
        assert driver.find_element_by_xpath("//h1[contains(text(),'Switch Window')]")
        driver.back()
        time.sleep(1)

    # Complete web form dropdown buttons click
    def test_15_completeWebForm_dropdown_click(self):
        driver = self.driver
        droppdown_elements = DropdownPage(driver)
        droppdown_elements.dropdown_button_click()
        time.sleep(1)
        droppdown_elements.completewebform_dropdown_button_click()
        time.sleep(1)
        assert driver.find_element_by_xpath("//h1[contains(text(),'Complete Web Form')]")
        driver.back()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Programming/QA/Projects/qa-py-formy-app-testing/reports'))
