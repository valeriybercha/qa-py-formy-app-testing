from Locators.locators import Locators


class CheckboxesPage():

    def __init__(self, driver):
        self.driver = driver

        self.input_checkbox_one_id = Locators.input_checkbox_one_id
        self.input_checkbox_two_id = Locators.input_checkbox_two_id
        self.input_checkbox_three_id = Locators.input_checkbox_three_id

    def checkbox_one(self):
        self.driver.find_element_by_id(self.input_checkbox_one_id)

    def checkbox_one_click(self):
        self.driver.find_element_by_id(self.input_checkbox_one_id).click()

    def checkbox_two_click(self):
        self.driver.find_element_by_id(self.input_checkbox_two_id).click()

    def checkbox_three_click(self):
        self.driver.find_element_by_id(self.input_checkbox_three_id).click()

    def checkbox_one_is_selected(self):
        self.driver.find_element_by_id(self.input_checkbox_one_id).is_selected()

    def checkbox_two_is_selected(self):
        self.driver.find_element_by_id(self.input_checkbox_two_id).is_selected()

    def checkbox_three_is_selected(self):
        self.driver.find_element_by_id(self.input_checkbox_three_id).is_selected()
