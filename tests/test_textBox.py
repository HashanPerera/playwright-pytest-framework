"""Implement the test logic here"""
from utils.data_reader import read_json

test_data = read_json("test_data.json")

def test_textBox_submit(text_box_page):

    #Launch the Text Box page
    text_box_page.navigate()

    #Fill in the "Full Name", "Email", "Current Address", "Permanent Address" input fields with sample data
    text_box_page.fill_full_name("John Doe")
    text_box_page.fill_email("john.doe@example.com")
    text_box_page.fill_current_address("123 Main Street")
    text_box_page.fill_permanent_address("456 Oak Avenue")

    #Submit the form
    text_box_page.submit_form()

    #Verify that the submitted data is displayed correctly on the page
    text_box_page.verify_submission("John Doe", "john.doe@example.com")

