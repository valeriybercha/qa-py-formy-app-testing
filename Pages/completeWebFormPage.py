from Locators.locators import Locators


class CompleteWebFormPage():

    def __init__(self, driver):
        self.driver = driver

        self.input_webForm_firstName_id = Locators.input_webForm_firstName_id
        self.input_webForm_lastName_id = Locators.input_webForm_lastName_id
        self.input_webForm_job_id = Locators.input_webForm_job_id
        self.input_webForm_radioButton1_id = Locators.input_webForm_radioButton1_id
        self.input_webForm_radioButton2_id = Locators.input_webForm_radioButton2_id
        self.input_webForm_radioButton3_id = Locators.input_webForm_radioButton3_id
        self.input_webForm_checkbox1_id = Locators.input_webForm_checkbox1_id
        self.input_webForm_checkbox2_id = Locators.input_webForm_checkbox2_id
        self.input_webForm_checkbox3_id = Locators.input_webForm_checkbox3_id
        self.select_webForm_selectMenu_id = Locators.select_webForm_selectMenu_id
        self.option_webForm_selectOption_xpath = Locators.option_webForm_selectOption_xpath
        self.option_webForm_0_1_xpath = Locators.option_webForm_0_1_xpath
        self.option_webForm_2_4_xpath = Locators.option_webForm_2_4_xpath
        self.option_webForm_5_9_xpath = Locators.option_webForm_5_9_xpath
        self.option_webForm_10_plus_xpath = Locators.option_webForm_10_plus_xpath
        self.input_webForm_datepicker_id = Locators.input_webForm_datepicker_id
        self.td_todayDate_xpath = Locators.td_todayDate_xpath
        self.a_webForm_button_xpath = Locators.a_webForm_button_xpath

    def firstName_input(self, first_name):
        self.driver.find_element_by_id(self.input_webForm_firstName_id).send_keys(first_name)

    def lastName_input(self, last_name):
        self.driver.find_element_by_id(self.input_webForm_lastName_id).send_keys(last_name)

    def job_input(self, job):
        self.driver.find_element_by_id(self.input_webForm_job_id).send_keys(job)

    def radio_button_1_click(self):
        self.driver.find_element_by_id(self.input_webForm_radioButton1_id).click()

    def radio_button_2_click(self):
        self.driver.find_element_by_id(self.input_webForm_radioButton2_id).click()

    def radio_button_3_click(self):
        self.driver.find_element_by_id(self.input_webForm_radioButton3_id).click()

    def radio_checkbox_1_click(self):
        self.driver.find_element_by_id(self.input_webForm_checkbox1_id).click()

    def radio_checkbox_2_click(self):
        self.driver.find_element_by_id(self.input_webForm_checkbox2_id).click()

    def radio_checkbox_3_click(self):
        self.driver.find_element_by_id(self.input_webForm_checkbox3_id).click()

    def dropdown_menu_click(self):
        self.driver.find_element_by_id(self.select_webForm_selectMenu_id).click()

    def dropdown_option_select_click(self):
        self.driver.find_element_by_xpath(self.option_webForm_selectOption_xpath).click()

    def dropdown_option_0_1_click(self):
        self.driver.find_element_by_xpath(self.option_webForm_0_1_xpath).click()

    def dropdown_option_2_4_click(self):
        self.driver.find_element_by_xpath(self.option_webForm_2_4_xpath).click()

    def dropdown_option_5_9_click(self):
        self.driver.find_element_by_xpath(self.option_webForm_5_9_xpath).click()

    def dropdown_option_10_plus_click(self):
        self.driver.find_element_by_xpath(self.option_webForm_10_plus_xpath).click()

    def datepicker_input(self, datepicker):
        self.driver.find_element_by_id(self.input_webForm_datepicker_id).send_keys(datepicker)

    def datepicker_click(self):
        self.driver.find_element_by_xpath(self.td_todayDate_xpath).click()

    def submit_button_click(self):
        self.driver.find_element_by_xpath(self.a_webForm_button_xpath).click()
