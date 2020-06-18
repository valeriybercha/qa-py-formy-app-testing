from Locators.locators import Locators


class DragdropPage():

    def __init__(self, driver):
        self.driver = driver

        self.img_dragdrop_id = Locators.img_dragdrop_id
        self.box_dragdrop_id = Locators.box_dragdrop_id
        self.text_dragdrop_xpath = Locators.text_dragdrop_xpath

    def drag_drop_img(self):
        self.driver.find_element_by_id(self.img_dragdrop_id)

    def drag_drop_box(self):
        self.driver.find_element_by_id(self.box_dragdrop_id)

    def drag_drop_text(self):
        self.driver.find_element_by_xpath(self.text_dragdrop_xpath)
