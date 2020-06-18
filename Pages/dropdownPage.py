from Locators.locators import Locators


class DropdownPage():

    def __init__(self, driver):
        self.driver = driver

        self.button_dropdown_page_id = Locators.button_dropdown_page_id
        self.a_dropdown_autocomplete_xpath = Locators.a_dropdown_autocomplete_xpath
        self.a_dropdown_buttons_xpath = Locators.a_dropdown_buttons_xpath
        self.a_dropdown_checkbox_xpath = Locators.a_dropdown_checkbox_xpath
        self.a_dropdown_datepicker_xpath = Locators.a_dropdown_datepicker_xpath
        self.a_dropdown_draganddrop_xpath = Locators.a_dropdown_draganddrop_xpath
        self.a_dropdown_dropdown_xpath = Locators.a_dropdown_dropdown_xpath
        self.a_dropdown_enabledisableelements_xpath = Locators.a_dropdown_enabledisableelements_xpath
        self.a_dropdown_fileupload_xpath = Locators.a_dropdown_fileupload_xpath
        self.a_dropdown_filedownload_xpath = Locators.a_dropdown_filedownload_xpath
        self.a_dropdown_keymousepress_xpath = Locators.a_dropdown_keymousepress_xpath
        self.a_dropdown_modal_xpath = Locators.a_dropdown_modal_xpath
        self.a_dropdown_pagesroll_xpath = Locators.a_dropdown_pagesroll_xpath
        self.a_dropdown_radiobutton_xpath = Locators.a_dropdown_radiobutton_xpath
        self.a_dropdown_switchwindow_xpath = Locators.a_dropdown_switchwindow_xpath
        self.a_dropdown_completewebform_xpath = Locators.a_dropdown_completewebform_xpath

    def dropdown_button_click(self):
        self.driver.find_element_by_id(self.button_dropdown_page_id).click()

    def autocomplete_dropdown_button_click(self):
        self.driver.find_element_by_xpath(self.a_dropdown_autocomplete_xpath).click()

    def buttons_dropdown_button_click(self):
        self.driver.find_element_by_xpath(self.a_dropdown_buttons_xpath).click()

    def checkbox_dropdown_button_click(self):
        self.driver.find_element_by_xpath(self.a_dropdown_checkbox_xpath).click()

    def datepicker_dropdown_button_click(self):
        self.driver.find_element_by_xpath(self.a_dropdown_datepicker_xpath).click()

    def draganddrop_dropdown_button_click(self):
        self.driver.find_element_by_xpath(self.a_dropdown_draganddrop_xpath).click()

    def dropdown_dropdown_button_click(self):
        self.driver.find_element_by_xpath(self.a_dropdown_dropdown_xpath).click()

    def enabledisableelems_dropdown_button_click(self):
        self.driver.find_element_by_xpath(self.a_dropdown_enabledisableelements_xpath).click()

    def fileupload_dropdown_button_click(self):
        self.driver.find_element_by_xpath(self.a_dropdown_fileupload_xpath).click()

    def filedownload_dropdown_button_click(self):
        self.driver.find_element_by_xpath(self.a_dropdown_filedownload_xpath).click()

    def keymousepress_dropdown_button_click(self):
        self.driver.find_element_by_xpath(self.a_dropdown_keymousepress_xpath).click()

    def modal_dropdown_button_click(self):
        self.driver.find_element_by_xpath(self.a_dropdown_modal_xpath).click()

    def pagescroll_dropdown_button_click(self):
        self.driver.find_element_by_xpath(self.a_dropdown_pagesroll_xpath).click()

    def radiobutton_dropdown_button_click(self):
        self.driver.find_element_by_xpath(self.a_dropdown_radiobutton_xpath).click()

    def switchwindow_dropdown_button_click(self):
        self.driver.find_element_by_xpath(self.a_dropdown_switchwindow_xpath).click()

    def completewebform_dropdown_button_click(self):
        self.driver.find_element_by_xpath(self.a_dropdown_completewebform_xpath).click()