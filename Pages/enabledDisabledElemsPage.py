from Locators.locators import Locators


class EnabledDisabledElemsPage():

    def __init__(self, driver):
        self.driver = driver

        self.input_disabled_id = Locators.input_disabled_id
        self.input_enabled_id = Locators.input_enabled_id


    def disabled_input_pass(self):
        self.driver.find_element_by_id(self.input_disabled_id).is_enabled()

    def enabled_input_pass(self):
        self.driver.find_element_by_id(self.input_enabled_id).is_enabled()