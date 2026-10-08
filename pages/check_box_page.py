from playwright.sync_api import expect

class CheckBoxPage:
    def __init__(self, page):
        self.page = page
        #Locators
        self.root_expander_opened = page.locator("xpath=//span[contains(@class, 'rc-tree-switcher rc-tree-switcher_open')]")
        self.root_expander_closed = page.locator("xpath=//span[contains(@class, 'rc-tree-switcher rc-tree-switcher_close')]")
        self.document_expander = page.locator("xpath=(//span[contains(@class, 'rc-tree-switcher rc-tree-switcher_close')])[2]")
        self.workspace_expander = page.locator("xpath=(//span[contains(@class, 'rc-tree-switcher rc-tree-switcher_close')])[3]")
        self.document_expander_opened = page.locator("xpath=(//span[contains(@class, 'rc-tree-switcher rc-tree-switcher_open')])[2]")
        self.workspace_expander_opened = page.locator("xpath=(//span[contains(@class, 'rc-tree-switcher rc-tree-switcher_open')])[3]")
        self.angular_expander = page.locator("xpath=(//span[contains(@class, 'rc-tree-checkbox')])[6]")
        self.result_text = page.locator("xpath=//div[@id='result']")
      
    def navigate(self):
        self.page.goto("https://demoqa.com/checkbox")

    def expand_root(self):
        expect(self.root_expander_opened).not_to_be_visible()
        expect(self.root_expander_closed).to_be_visible()
        self.root_expander_closed.click()

    def expand_Documents(self):
        expect(self.document_expander).to_be_visible()
        self.document_expander.click()
    
    def expand_Workspace(self):
        expect(self.document_expander_opened).to_be_visible()
        expect(self.workspace_expander).to_be_visible()
        self.workspace_expander.click()

    def check_Angular(self):
        expect(self.workspace_expander_opened).to_be_visible()
        expect(self.angular_expander).to_be_visible()
        self.angular_expander.check()
        expect(self.angular_expander).to_be_checked()
        assert self.result_text.inner_text() == "You have selected :\nangular"
    
    def uncheck_Angular(self):
        expect(self.workspace_expander_opened).to_be_visible()
        expect(self.angular_expander).to_be_visible()
        self.angular_expander.check()
        expect(self.angular_expander).to_be_checked()
        self.angular_expander.uncheck()
        expect(self.angular_expander).not_to_be_checked()
        expect(self.result_text).to_be_hidden()
        