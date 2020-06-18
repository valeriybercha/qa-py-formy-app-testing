import unittest
import HtmlTestRunner
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver


class DragdropTest(unittest.TestCase):

    def test_01_drag_drop(self):
        self.driver = webdriver.Chrome('D:/Programming/QA/Projects/qa-py-formy-app-testing/drivers/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get("https://formy-project.herokuapp.com/dragdrop")

        image = self.driver.find_element_by_id('image')
        drop_box = self.driver.find_element_by_id('box')

        ActionChains(self.driver).drag_and_drop(image, drop_box).perform()

        time.sleep(2)

        assert self.driver.find_element_by_xpath("//p[contains(text(),'Dropped!')]")

        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Programming/QA/Projects/qa-py-formy-app-testing/reports'))
