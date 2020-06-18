from Locators.locators import Locators


class DatepickerPage():

    def __init__(self, driver):
        self.driver = driver

        self.input_datepicker_checkbox_id = Locators.input_datepicker_checkbox_id
        self.datepicker_today_date_xpath = Locators.datepicker_today_date_xpath
        self.datepicker_other_date_xpath = Locators.datepicker_other_date_xpath

    def date_input(self, send_date):
        td = self.driver.find_element_by_id(self.input_datepicker_checkbox_id)
        td.clear()
        td.click()
        td.send_keys(send_date)

    def datepicker_today_date(self):
        self.driver.find_element_by_xpath(self.datepicker_today_date_xpath)

    def datepicker_other_date(self):
        self.driver.find_element_by_xpath(self.datepicker_other_date_xpath)
