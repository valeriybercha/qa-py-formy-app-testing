from unittest import TestLoader, TestSuite, TextTestRunner
import unittest
import HtmlTestRunner
from Tests.checkboxes import CheckboxesTest
from Tests.autocomplete import AutocompleteTest
from Tests.buttons import ButtonsTest
from Tests.completeWebForm import CompleteWebFormTest
from Tests.datepicker import DatepickerTest
from Tests.dragdrop import DragdropTest
from Tests.dropdown import DropdownTest
from Tests.enabledDisabledElems import EnabledDisabledElemsTest
from Tests.fileUpload import FileUploadTest
from Tests.modal import ModalTest
from Tests.radioButtons import RadioButtonsTest
from Tests.scroll import ScrollTest
from Tests.switchWindows import SwitchWindowsTest

# Running all tests suite

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Programming/QA/Projects/qa-py-formy-app-testing/reports'))

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(CheckboxesTest),
        loader.loadTestsFromTestCase(AutocompleteTest),
        loader.loadTestsFromTestCase(ButtonsTest),
        loader.loadTestsFromTestCase(CompleteWebFormTest),
        loader.loadTestsFromTestCase(DatepickerTest),
        loader.loadTestsFromTestCase(DragdropTest),
        loader.loadTestsFromTestCase(DropdownTest),
        loader.loadTestsFromTestCase(EnabledDisabledElemsTest),
        loader.loadTestsFromTestCase(FileUploadTest),
        loader.loadTestsFromTestCase(ModalTest),
        loader.loadTestsFromTestCase(RadioButtonsTest),
        loader.loadTestsFromTestCase(ScrollTest),
        loader.loadTestsFromTestCase(SwitchWindowsTest)
    ))

    runner = TextTestRunner()
    runner.run(suite)