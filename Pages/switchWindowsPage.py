from Locators.locators import Locators


class SwitchWindowsPage():

    def __init__(self, driver):
        self.driver = driver

        self.button_switchWindow_newTab_id = Locators.button_switchWindow_newTab_id
        self.button_switchWindow_alert_id = Locators.button_switchWindow_alert_id

    def newTab_button_click(self):
        self.driver.find_element_by_id(self.button_switchWindow_newTab_id).click()

    def alert_button_click(self):
        self.driver.find_element_by_id(self.button_switchWindow_alert_id).click()

