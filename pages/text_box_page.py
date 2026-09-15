from playwright.sync_api import Page

class TextBoxPage:

    def __init__(self, page: Page):
        self.page = page

        # using ID selector for the "Full Name" input field
        self.full_name_input = page.locator("id=userName")
        # using ID selector for the "Email" input field
        self.email_input = page.locator("#userEmail")
        # using ID selector for the "Current Address" input field
        self.current_address_input = page.locator("#currentAddress")
        self.permanent_address_input = page.locator("#permanentAddress")
        # using role selector for the "Submit" button
        self.submit_button = page.get_by_role("button", name="Submit")

        # Output elements
        self.name_output = page.locator("#name")
        self.email_output = page.locator("#email")

    def navigate(self):
        self.page.goto("https://demoqa.com/text-box")
    
    def fill_full_name(self, full_name:str):
        self.full_name_input.fill(full_name)

    def fill_email(self, email:str):
        self.email_input.fill(email)

    def fill_current_address(self, current_address:str):
        self.current_address_input.fill(current_address)

    def fill_permanent_address(self, permanent_address:str):
        self.permanent_address_input.fill(permanent_address)

    def submit_form(self):
        self.submit_button.click()

    def verify_submission(self, full_name:str, email:str):
        assert self.name_output.inner_text() == f"Name:{full_name}"
        assert self.email_output.inner_text() == f"Email:{email}"