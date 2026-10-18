import pytest

from playwright.sync_api import Page, expect

class WebTablesPage:
    def __init__(self, page: Page):
        self.page = page
        self.web_tables_link = 'https://demoqa.com/webtables'

        self.form_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "age": "30",
            "salary": "50000",
            "department": "IT"
        }

        #locators
        self.add_button = page.locator("id=addNewRecordButton")
        self.first_name_input = page.locator("id=firstName")
        self.last_name_input = page.locator("id=lastName")
        self.email_input = page.locator("id=userEmail")
        self.age_input = page.locator("id=age")
        self.salary_input = page.locator("id=salary")
        self.department_input = page.get_by_placeholder("department")
        self.submit_button = page.locator("id=submit")

        self.result_coloumn = page.locator("xpath=//tr[4]//td[1]")

    def navigate(self):
        self.page.goto(self.web_tables_link)

    def fill_form(self, form_data):
        self.add_button.click()
        self.first_name_input.fill(form_data["first_name"])
        self.last_name_input.fill(form_data["last_name"])
        self.email_input.fill(form_data["email"])
        self.age_input.fill(form_data["age"])
        self.salary_input.fill(form_data["salary"])
        self.department_input.fill(form_data["department"])
        self.submit_button.click()
        expect(self.result_coloumn).to_contain_text(form_data["first_name"])
    
    
    """
    def search_record(self, search_term):
        self.page.locator("id=searchBox").fill(search_term)
        #expect(self.page.locator("id=searchBox")).to_have_value(search_term)
    
    def edit_record(self, row_index, data):
        self.page.locator("id=searchBox").fill(data["email"])
        self.page.locator(f"xpath=//div[@class='rt-tr-group'][{row_index}]//span[@title='Edit']").click()
        self.salary_input.fill(data["salary1"])
        self.submit_button.click()
        expect(page.locator("xpath=//*[@id=root]/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr/td[5]")).to_contain_text(data["salary1"])

        """