from Locators.locators import Locators


class RadioButtonsPage():

    def __init__(self, driver):
        self.driver = driver

        self.input_radio_one_xpath = Locators.input_radio_one_xpath
        self.input_radio_two_xpath = Locators.input_radio_two_xpath
        self.input_radio_three_xpath = Locators.input_radio_three_xpath

    def radio_button_one_click(self):
        self.driver.find_element_by_xpath(self.input_radio_one_xpath).click()

    def radio_button_two_click(self):
        self.driver.find_element_by_xpath(self.input_radio_two_xpath).click()

    def radio_button_three_click(self):
        self.driver.find_element_by_xpath(self.input_radio_three_xpath).click()

    def radio_button_one_is_selected(self):
        self.driver.find_element_by_xpath(self.input_radio_one_xpath).is_selected()

    def radio_button_two_is_selected(self):
        self.driver.find_element_by_xpath(self.input_radio_two_xpath).is_selected()

    def radio_button_three_is_selected(self):
        self.driver.find_element_by_xpath(self.input_radio_three_xpath).is_selected()