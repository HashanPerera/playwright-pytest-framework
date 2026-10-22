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
        self.search_data = page.locator("id=searchBox")
        self.searched_email = page.locator("xpath=//tr//td[4]")

        self.edit_data = page.locator("id=edit-record-1")
        self.edit_lastname = page.locator("id=lastName")
        self.edit_form_submit = page.locator("id=submit")
        self.edited_lastname = page.locator("xpath=//tr//td[2]")

        self.delete_record = page.locator("id=delete-record-1")
        self.deleted_row = page.locator("xpath=//tbody//tr")


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

    def search_record(self):
        self.search_data.fill("Cierra")
        expect(self.searched_email).to_contain_text("cierra@example.com")
 
    def edit_record(self):
        self.search_data.fill("cierra@example.com")
        expect(self.searched_email).to_contain_text("cierra@example.com")
        self.edit_data.click()
        self.edit_lastname.clear()
        self.edit_lastname.fill("Vegan")
        self.edit_form_submit.click()
        expect(self.edited_lastname).to_contain_text("Vegan")

    def delete_table_row(self):
        self.search_data.fill("cierra@example.com")
        expect(self.searched_email).to_contain_text("cierra@example.com")
        self.delete_record.click()
        expect(self.deleted_row).to_be_hidden()




    