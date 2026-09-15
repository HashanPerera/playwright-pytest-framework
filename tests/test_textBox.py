"""Implement the test logic here"""
import pytest
from utils.data_reader import read_json

test_data = read_json("test_data/text_box_data.json")

@pytest.mark.parametrize("data", test_data)
def test_textBox_submit(text_box_page, data):

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
    text_box_page.verify_submission(data["full_name"], data["email"])

