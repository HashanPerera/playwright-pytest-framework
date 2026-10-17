import pytest

def test_double_click(button_page):
    button_page.navigate()
    button_page.double_Click_button()

def test_right_click(button_page):
    button_page.navigate()
    button_page.right_Click_button()

def test_dynamic_click(button_page):
    button_page.navigate()
    button_page.dynamic_Click_button()
