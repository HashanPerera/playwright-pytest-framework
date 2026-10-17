from playwright.sync_api import expect

class Radio_button_page:
    def __init__(self,page):

        self.page = page
        self.radio_button_page_link = 'https://demoqa.com/radio-button'
        
        #Locators
        self.yes_radio_button = page.locator("id=yesRadio")
        self.impressive_radio_button = page.locator("id=impressiveRadio")
        self.no_radio_button = page.locator("id=noRadio")
        self.result_text = page.locator("//p[contains(@class, 'mt-3')]")
        self.result_yes_no_text = page.locator("xpath=//span[contains(@class, 'text-success')]")

    def navigate(self):
        self.page.goto(self.radio_button_page_link)

    def click_yes_radio_button(self):
        self.yes_radio_button.click()
        expect(self.result_text).to_be_visible()
        expect(self.result_yes_no_text).to_have_text("Yes")

    def click_impressive_radio_button(self):
        self.impressive_radio_button.click()
        expect(self.result_text).to_be_visible()
        expect(self.result_yes_no_text).to_have_text("Impressive")

    def click_no_radio_button(self):
        expect(self.no_radio_button).to_be_disabled()