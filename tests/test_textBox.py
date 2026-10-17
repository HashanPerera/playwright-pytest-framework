"""Implement the test logic here"""
import pytest
from utils.data_reader import read_json
from playwright.sync_api import expect

test_data = read_json("test_data/text_box_data.json")

@pytest.mark.parametrize("data", test_data)

def test_textBox_submit(text_box_page, data):
    #TC-TextBox-001
    #Launch the Text Box page
    text_box_page.navigate()

    #Fill in the "Full Name", "Email", "Current Address", "Permanent Address" input fields with sample data
    text_box_page.fill_full_name(data["full_name"])
    text_box_page.fill_email(data["email"])
    text_box_page.fill_current_address(data["current_address"])
    text_box_page.fill_permanent_address(data["permanent_address"])

    #Submit the form
    text_box_page.submit_form()

    #Verify that the submitted data is displayed correctly on the page
    assert text_box_page.name_output.inner_text() == f"Name:{data['full_name']}"
    assert text_box_page.email_output.inner_text() == f"Email:{data['email']}"
    assert text_box_page.current_address_output.inner_text() == f"Current Address :{data['current_address']}"
    assert text_box_page.permanent_address_output.inner_text() == f"Permananet Address :{data['permanent_address']}"


def test_textBox_invalid_email(text_box_page):
    #TC-TextBox-002
    #Launch the Text Box page
    text_box_page.navigate()

    #Fill in the "Full Name" and "Email" input fields with sample data, but provide an invalid email format
    text_box_page.fill_full_name("John Doe")
    """ input_border_color = text_box_page.email_input.evaluate(
    "(element) => getComputedStyle(element).borderColor"
    )
    print(input_border_color) """
    
    #verify invalid email error
    text_box_page.email_input.fill("invalid-email-format")
    text_box_page.submit_button.click()
    expect(text_box_page.invalid_email_class_name).to_have_class("mr-sm-2 field-error form-control")
    """ input_border_color = text_box_page.email_input.evaluate(
    "(element) => getComputedStyle(element).borderColor"
    )
    print(input_border_color) """

def test_textBox_with_one_field(text_box_page):
    #TC-TextBox-003
    #Launch the Text Box page
    text_box_page.navigate()

    #Fill in the "Full Name" and "Email" input fields with special characters
    text_box_page.fill_full_name("John Doe")

    #Submit the form
    text_box_page.submit_form()

    #Verify that the submitted data is displayed correctly on the page
    assert text_box_page.name_output.inner_text() == "Name:John Doe"
    expect(text_box_page.email_output).not_to_be_visible()
    expect(text_box_page.current_address_output).to_be_hidden()
    expect(text_box_page.permanent_address_output).not_to_be_visible()

def test_textBox_empty_fields(text_box_page):
    #TC-TextBox-004
    #Launch the Text Box page
    text_box_page.navigate()

    #Submit the form without filling any fields
    text_box_page.submit_form()

    #Verify that appropriate error messages are displayed for each empty field
    expect(text_box_page.name_output).not_to_be_visible()
    expect(text_box_page.email_output).not_to_be_visible()
    expect(text_box_page.current_address_output).to_be_hidden()
    expect(text_box_page.permanent_address_output).to_be_hidden()
    