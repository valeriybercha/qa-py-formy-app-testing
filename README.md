# Test automation framework using Python, Selenium, Unittest, HTML-reports.
GUI functional testing of Formy (https://formy-project.herokuapp.com/) web app using Selenium Webdriver, Python, Unittest and HTML-reports. 
The entire framework is based on Page Object Model (POM) design pattern with separate project directories (pages, tests, locators, reports etc.) for reducing code duplication and improving test maintenance. You can either run a specified test or all tests at once with HTML reports generated after test completion.

### Page Object Model (POM) structure:

- [drivers](https://github.com/valeriybercha/qa-py-formy-app-testing/tree/master/drivers) - drivers (Chrome, Firefox) location directory
- [Locators](https://github.com/valeriybercha/qa-py-formy-app-testing/tree/master/Locators) - locators directory
- [Pages](https://github.com/valeriybercha/qa-py-formy-app-testing/tree/master/Pages) - project pages directory
- [reports](https://github.com/valeriybercha/qa-py-formy-app-testing/tree/master/reports) - HTML reports directory
- [Tests](https://github.com/valeriybercha/qa-py-formy-app-testing/tree/master/Tests) - project tests directory

### Usage:
To run all tests from the test suite use the allTestsRunner.py file from command prompt (cmd) with the following command:
```sh
python -m allTestsRunner
```
To run a specified test from the Tests directory use the following command:
```sh
python -m Tests.<test_to_run>
```
NOTE: For HTML reports to be generated it is recommended to run the commands directly from the command prompt (cmd) other than from IDE.

Screenshot:
![Formy app testing screenshot](https://github.com/valeriybercha/qa-py-formy-app-testing/blob/master/screenshot.jpg)