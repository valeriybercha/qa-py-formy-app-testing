from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from Pages.fileUploadPage import FileUploadPage
from Locators.locators import Locators


class FileUploadTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:/Programming/QA/Projects/qa-py-formy-app-testing/drivers/chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(Locators.baseURL + 'fileupload')

    # Send keys to file upload input field and reset the information
    def test_01_file_input_and_reset(self):
        driver = self.driver
        file_upload = FileUploadPage(driver)
        file_upload.file_upload_send_keys(Locators.file_upload)
        time.sleep(1)
        file_upload.file_upload_reset_btn_click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Programming/QA/Projects/qa-py-formy-app-testing/reports'))
