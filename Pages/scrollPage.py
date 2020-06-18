from Locators.locators import Locators


class ScrollPage():

    def __init__(self, driver):
        self.driver = driver

        self.input_scroll_name_id = Locators.input_scroll_name_id
        self.input_scroll_date_id = Locators.input_scroll_date_id

    def scroll_name_locator(self):
        self.driver.find_element_by_id(self.input_scroll_name_id)

    def scroll_name_input(self, name):
        self.driver.find_element_by_id(self.input_scroll_name_id).send_keys(name)

    def scroll_date_input(self, date):
        self.driver.find_element_by_id(self.input_scroll_date_id).send_keys(date)

