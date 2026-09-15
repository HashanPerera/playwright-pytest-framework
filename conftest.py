import pytest
from playwright.sync_api import Page, Browser, sync_playwright

from pages.text_box_page import TextBoxPage


@pytest.fixture
def page() -> Page:

    with sync_playwright() as playwright:

        browser: Browser = playwright.chromium.launch(
            headless=False
        )

        context = browser.new_context()

        page = context.new_page()

        yield page

        context.close()
        browser.close()


@pytest.fixture
def text_box_page(page):
    return TextBoxPage(page)