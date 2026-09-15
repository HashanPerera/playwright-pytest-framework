from playwright.sync_api import Page

class GooglePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        #Navigate to the Google homepage
        self.page.goto("https://www.google.com")

    def dismiss_cookie_banner(self):
        #Click the "Reject all" button to dismiss the cookie consent banner
        self.page.get_by_role("button", name="Reject all").click()

    def search(self, text: str):
        #Get the search box and perform a search
        search_box = self.page.get_by_role("combobox")
        #Check if the search box is visible
        assert search_box.is_visible()
        #Fill the search box with the provided text and press "Enter"
        search_box.fill(text)
        search_box.press("Enter")