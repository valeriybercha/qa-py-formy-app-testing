from selenium import webdriver
import unittest
import HtmlTestRunner
from Pages.datepickerPage import DatepickerPage
from Locators.locators import Locators
from datetime import date
import random


# Today's date function
def today_date():
    dt = date.today()
    dt_formatted = dt.strftime("%m/%d/%Y")
    return dt_formatted


# Random date function (Date: from 1 to 28, Month: from 1 to 12)
def random_date():
    random_day = random.randint(1, 28)
    random_month = random.randint(1, 12)
    if len(str(random_day)) < 2:
        random_day = "0" + str(random_day)
    if len(str(random_month)) < 2:
        random_month = "0" + str(random_month)
    random_date = str(random_month) + "/" + str(random_day) + "/2020"
    return random_date


class DatepickerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:/Programming/QA/Projects/qa-py-formy-app-testing/drivers/chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(Locators.baseURL + 'datepicker')

    # Today's date selection test case
    def test_01_today_date(self):
        driver = self.driver
        today_date_selection = DatepickerPage(driver)
        today_date_selection.date_input(today_date())
        today_date_selection.datepicker_today_date()

    # Other date selection test case
    def test_02_other_date(self):
        driver = self.driver
        today_date_selection = DatepickerPage(driver)
        today_date_selection.date_input(random_date())
        today_date_selection.datepicker_other_date()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Programming/QA/Projects/qa-py-formy-app-testing/reports'))
