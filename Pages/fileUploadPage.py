from Locators.locators import Locators


class FileUploadPage():

    def __init__(self, driver):
        self.driver = driver

        self.input_upload_id = Locators.input_upload_id
        self.button_upload_reset_xpath = Locators.button_upload_reset_xpath
        self.button_upload_choose_xpath = Locators.button_upload_choose_xpath

    def file_upload_input(self):
        self.driver.find_element_by_id(self.input_upload_id)

    def file_upload_send_keys(self, test_file):
        self.driver.find_element_by_id(self.input_upload_id).send_keys(test_file)

    def file_upload_choose_btn_click(self):
        self.driver.find_element_by_xpath(self.button_upload_choose_xpath).click()

    def file_upload_reset_btn_click(self):
        self.driver.find_element_by_xpath(self.button_upload_reset_xpath).click()
