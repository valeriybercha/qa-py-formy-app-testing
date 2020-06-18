from selenium import webdriver


class Locators():

    # Base url
    baseURL = 'https://formy-project.herokuapp.com/'

    # Chrome webdriver
    driver = webdriver.Chrome('D:/Programming/QA/Projects/qa-py-formy-app-testing/drivers/chromedriver.exe')

    # 01) Autocomplete page locators
    input_autocomplete_id = 'autocomplete'
    dropdown_autocomplete_class = 'pac-icon'
    input_street_number_id = 'street_number'
    input_route_id = 'route'
    input_locality_id = 'locality'
    input_administrative_area_level_1_id = 'administrative_area_level_1'
    input_postal_code_id = 'postal_code'
    input_country_id = 'country'
    full_address_text = 'Komarova steet, 1, Chernivtsi, Ukraine'

    # 02) Buttons page locators

    # First row buttons
    button_primary_xpath = "//button[contains(text(), 'Primary')]"
    button_success_xpath = "//button[contains(text(), 'Success')]"
    button_info_xpath = "//button[contains(text(), 'Info')]"
    button_warning_xpath = "//button[contains(text(), 'Warning')]"
    button_danger_xpath = "//button[contains(text(), 'Danger')]"
    button_link_xpath = "//button[contains(text(), 'Link')]"

    # Second row buttons
    button_left_xpath = "//button[contains(text(), 'Left')]"
    button_middle_xpath = "//button[contains(text(), 'Middle')]"
    button_right_xpath = "//button[contains(text(), 'Right')]"

    # Third row buttons
    button_one_xpath = "//button[contains(text(), '1')]"
    button_two_xpath = "//button[contains(text(), '2')]"
    button_dropdown_id = "btnGroupDrop1"
    a_dropdown_one_xpath = "//a[contains(text(),'Dropdown link 1')]"
    a_dropdown_two_xpath = "//a[contains(text(),'Dropdown link 2')]"

    # 03) Checkboxes page locators
    input_checkbox_one_id = 'checkbox-1'
    input_checkbox_two_id = 'checkbox-2'
    input_checkbox_three_id = 'checkbox-3'

    # 04) Datepicker page locators
    input_datepicker_checkbox_id = 'datepicker'
    datepicker_today_date_xpath = '//td[@class="today active day"]'
    datepicker_other_date_xpath = '//td[@class="active day"]'

    # 05) Drag and drop page locators
    img_dragdrop_id = 'image'
    box_dragdrop_id = 'box'
    text_dragdrop_xpath = "//p[contains(text(),'Dropped!')]"

    # 06) Dropdown page locators
    button_dropdown_page_id = 'dropdownMenuButton'
    a_dropdown_autocomplete_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Autocomplete')]"
    a_dropdown_buttons_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Buttons')]"
    a_dropdown_checkbox_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Checkbox')]"
    a_dropdown_datepicker_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Datepicker')]"
    a_dropdown_draganddrop_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Drag and Drop')]"

    a_dropdown_dropdown_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Dropdown')]"
    a_dropdown_enabledisableelements_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Enabled and disabled elements')]"
    a_dropdown_fileupload_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'File Upload')]"
    a_dropdown_filedownload_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'File Download')]"
    a_dropdown_keymousepress_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Key and Mouse Press')]"

    a_dropdown_modal_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Modal')]"
    a_dropdown_pagesroll_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Page Scroll')]"
    a_dropdown_radiobutton_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Radio Button')]"
    a_dropdown_switchwindow_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Switch Window')]"
    a_dropdown_completewebform_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Complete Web Form')]"

    # 07) Enabled and disabled page locators
    input_disabled_id = 'disabledInput'
    input_enabled_id = 'input'

    # 08) File upload page locators
    file_upload = 'D:\Programming\QA\Projects\qa-py-formy-app-testing\Locators\zest_file.txt'
    input_upload_id = 'file-upload-field'
    button_upload_choose_xpath = "//button[contains(text(),'Choose')]"
    button_upload_reset_xpath = "//button[contains(text(),'Reset')]"

    # 09) Keyboard and mouse inputs page locators
    input_keyboardMouse_id = 'name'
    button_keyborardMouse_id = 'button'

    # 10) Modal page locators
    button_modal_id = 'modal-button'
    h_modal_id = 'exampleModalLabel'

    # 11) Scroll page selectors
    input_scroll_name_id = 'name'
    input_scroll_date_id = 'name'

    # 12) Radio buttons page locators
    input_radio_one_xpath = "//input[@value='option1']"
    input_radio_two_xpath = "//input[@value='option2']"
    input_radio_three_xpath = "//input[@value='option3']"

    # 13) Switch windows page locators
    button_switchWindow_newTab_id = 'new-tab-button'
    button_switchWindow_alert_id = 'alert-button'

    # 14) Complete web form page locators
    input_webForm_firstName_id = 'first-name'
    input_webForm_lastName_id = 'last-name'
    input_webForm_job_id = 'job-title'

    input_webForm_radioButton1_id = 'radio-button-1'
    input_webForm_radioButton2_id = 'radio-button-2'
    input_webForm_radioButton3_id = 'radio-button-3'

    input_webForm_checkbox1_id = 'checkbox-1'
    input_webForm_checkbox2_id = 'checkbox-2'
    input_webForm_checkbox3_id = 'checkbox-3'

    select_webForm_selectMenu_id = 'select-menu'
    option_webForm_selectOption_xpath = "//option[contains(text(),'Select an option')]"
    option_webForm_0_1_xpath = "//option[contains(text(),'0-1')]"
    option_webForm_2_4_xpath = "//option[contains(text(),'2-4')]"
    option_webForm_5_9_xpath = "//option[contains(text(),'5-9')]"
    option_webForm_10_plus_xpath = "//option[contains(text(),'10+')]"

    input_webForm_datepicker_id = 'datepicker'
    td_todayDate_xpath = "/html[1]/body[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[4]"

    a_webForm_button_xpath = "//a[contains(text(), 'Submit')]"
