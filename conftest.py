import pytest
from playwright.sync_api import Page, Browser, sync_playwright

from pages.text_box_page import TextBoxPage
from pages.check_box_page import CheckBoxPage
from pages.radio_button_page import Radio_button_page
from pages.buttons_page import Button_page
from pages.practice_form_page import Practice_FormPage
from pages.web_tables_page import WebTablesPage
from pages.broken_links_images import BrokenLinkImages


@pytest.fixture
def page() -> Page:

    with sync_playwright() as playwright:

        browser: Browser = playwright.chromium.launch(
            headless=False
        )

        context = browser.new_context()

        page = context.new_page()

        main_link = "https://demoqa.com/"

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

@pytest.fixture
def button_page(page):
    return Button_page(page)

@pytest.fixture
def practice_form_page(page):
    return Practice_FormPage(page)

@pytest.fixture
def web_table_page(page):
    return WebTablesPage(page)

@pytest.fixture
def broken_link_image(page):
    return BrokenLinkImages(page)