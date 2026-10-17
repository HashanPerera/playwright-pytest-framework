import pytest
from playwright.sync_api import Page, Browser, sync_playwright

from pages.text_box_page import TextBoxPage
from pages.check_box_page import CheckBoxPage
from pages.radio_button_page import Radio_button_page


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

@pytest.fixture
def check_box_page(page):
    return CheckBoxPage(page) 

@pytest.fixture
def radio_button_page(page):
    return Radio_button_page(page)