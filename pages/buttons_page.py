from playwright.sync_api import Page, expect

class Button_page:
    def __init__(self, page):
        self.page = page
        self.button_page_link = 'https://demoqa.com/buttons'
        #Locators
        self.double_click_button = page.locator("id=doubleClickBtn")
        self.right_click_button = page.locator("id=rightClickBtn")
        self.dynamic_click_button = page.locator("xpath=//button[text()='Click Me']")
        self.expected_double_click_message = page.locator("id=doubleClickMessage")
        self.expected_right_click_message = page.locator("id=rightClickMessage")
        self.expected_dynamic_click_message = page.locator("id=dynamicClickMessage")

    def navigate(self):
        self.page.goto(self.button_page_link)
    
    def double_Click_button(self):
        self.double_click_button.dblclick()
        expect(self.expected_double_click_message).to_be_visible()
        expect(self.expected_double_click_message).to_have_text("You have done a double click")

    def right_Click_button(self):
        self.right_click_button.click(button="right")
        expect(self.expected_right_click_message).to_be_visible()
        expect(self.expected_right_click_message).to_have_text("You have done a right click")

    def dynamic_Click_button(self):
        self.dynamic_click_button.click()
        expect(self.expected_dynamic_click_message).to_be_visible()
        expect(self.expected_dynamic_click_message).to_have_text("You have done a dynamic click")