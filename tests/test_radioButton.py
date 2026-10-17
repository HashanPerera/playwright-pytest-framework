import pytest

def test_radioButton_click_yes(radio_button_page):
    #TC-RadioButton-001
    #Launch the Radio Button page
    radio_button_page.navigate()

    #Click the "Yes" radio button
    radio_button_page.click_yes_radio_button()

def test_radioButton_click_impressive(radio_button_page):
    #TC-RadioButton-002
    #Launch the Radio Button page
    radio_button_page.navigate()

    #Click the "Impressive" radio button
    radio_button_page.click_impressive_radio_button()

def test_radioButton_click_no(radio_button_page):
    #TC-RadioButton-003
    #Launch the Radio Button page
    radio_button_page.navigate()

    #Click the "No" radio button
    radio_button_page.click_no_radio_button()   