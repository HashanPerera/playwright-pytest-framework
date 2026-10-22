import pytest
from playwright.sync_api import Page, expect

class BrokenLinkImages:
    def __init__(self, page: Page):
        self.page = page
        self.broken_link_page = 'https://demoqa.com/broken'

        #locator
        self.broken_image = page.locator("xpath=//img[2]")
        self.image = page.locator("img").first

    def navigate(self):
        self.page.goto(self.broken_link_page)

    def check_broken_image(self):
        expect(self.broken_image).to_be_visible()
        assert self.broken_image.evaluate("(img) => img.complete && img.naturalWidth == 0")

        """Key idea:
        - naturalWidth == 0 → image failed to load / broken ❌
        """

    def check_unbroken_image(self):
        expect(self.image).to_be_visible()
        assert self.image.evaluate("(img) => img.complete && img.naturalWidth > 0")

        """Key idea:
        - naturalWidth > 0 → image loaded successfully ✅
        """