from Locators.locators import Locators


class ModalPage():

    def __init__(self, driver):
        self.driver = driver

        self.button_modal_id = Locators.button_modal_id
        self.h_modal_id = Locators.h_modal_id


    def modal_button_click(self):
        self.driver.find_element_by_id(self.button_modal_id).click()

    def modal_header(self):
        self.driver.find_element_by_id(self.h_modal_id)

