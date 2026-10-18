from playwright.sync_api import expect

class Practice_FormPage:
    def __init__(self, page):

        self.page = page
        self.formPage_link = 'https://demoqa.com/automation-practice-form'

        #data to fill in the form
        self.data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "gender": "Male",
            "user_number": "1234567890",
            "date_of_birth": "1990-01-01",
            "subject": "Computer Science",
            "hobbies": "Reading",
            "picture_path": "path/to/picture.jpg",
            "current_address": "123 Main Street",
            "state": "Haryana",
            "city": "Karnal"
        }

        #locators
        self.first_name = page.locator("id=firstName")
        self.last_name = page.locator("id=lastName")
        self.email = page.locator("id=userEmail")
        self.gender_male = page.locator("id=gender-radio-1")
        self.user_number = page.locator("id=userNumber")
        self.date_of_birth = page.locator("id=dateOfBirthInput")
        self.subjects_input = page.locator("id=subjectsInput")
        self.hobbies_reading = page.locator("id=hobbies-checkbox-2")
        self.picture_upload = page.locator("id=uploadPicture")
        self.current_address = page.locator("id=currentAddress")
        self.state_dropdown = page.locator("id=state")
        self.state_select = page.locator("id=react-select-3-input")
        self.city_dropdown = page.locator("id=city")
        self.city_select = page.locator("id=react-select-4-input")
        self.submit_button = page.locator("id=submit")

        self.dialog_frame = page.locator("div[role=dialog]")
        self.success_message = page.locator("xpath=//*[@id=example-modal-sizes-title-lg]")
        #self.success_message = page.locator("xpath=//*[@id='google_ads_top_frame']").content_frame.locator("id=example-modal-sizes-title-lg")   

    def navigate(self):
        self.page.goto(self.formPage_link)

    def fill_form(self, data):
        self.first_name.fill(data["first_name"])
        self.last_name.fill(data["last_name"])
        self.email.fill(data["email"])
        self.gender_male.check()
        self.user_number.fill(data["user_number"])
        #self.date_of_birth.fill(data["date_of_birth"])
        #expect(self.date_of_birth).to_have_value(data["date_of_birth"])
        self.subjects_input.fill(data["subject"])
        expect(self.subjects_input).to_have_value(data["subject"])
        #self.hobbies_reading.check()
        #self.picture_upload.set_input_files(data["picture_path"])
        self.current_address.fill(data["current_address"])
        self.state_dropdown.click()
        self.state_select.fill(data["state"])
        self.page.keyboard.press("Enter")
        expect(self.state_dropdown).to_contain_text(data["state"])

        # Verify City is initially disabled
        #self.city_select.fill(data["city"])
        #expect(self.city_select).to_have_value(data["city"])
        self.city_dropdown.click()
        self.city_select.fill(data["city"])
        self.page.keyboard.press("Enter")
        expect(self.city_dropdown).to_contain_text(data["city"])

        self.submit_button.click()
        

        #expect(self.dialog_frame).to_be_visible()
        expect(self.success_message).to_contain_text("Thanks for submitting the form")