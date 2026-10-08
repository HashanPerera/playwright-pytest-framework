import pytest

def test_checkBox_expand_root(check_box_page):
    #TC-CheckBox-001
    #Launch the Check Box page
    check_box_page.navigate()

    #Expand the root checkbox
    check_box_page.expand_root()

def test_checkBox_expand_documents(check_box_page):
    #TC-CheckBox-002
    #Launch the Check Box page
    check_box_page.navigate()

    #Expand the root checkbox
    check_box_page.expand_root()

    #Expand the "Documents" checkbox
    check_box_page.expand_Documents()

def test_checkBox_expand_workspace(check_box_page):
    #TC-CheckBox-003
    #Launch the Check Box page
    check_box_page.navigate()

    #Expand the root checkbox
    check_box_page.expand_root()

    #Expand the "Documents" checkbox
    check_box_page.expand_Documents()

    #Expand the "Workspace" checkbox
    check_box_page.expand_Workspace()

def test_checking_angular_checkbox(check_box_page):
    #TC-CheckBox-004
    #Launch the Check Box page
    check_box_page.navigate()

    #Expand the root checkbox
    check_box_page.expand_root()

    #Expand the "Documents" checkbox
    check_box_page.expand_Documents()

    #Expand the "Workspace" checkbox
    check_box_page.expand_Workspace()

    #Expand the "Angular" checkbox
    check_box_page.check_Angular()

def test_unchecking_angular_checkbox(check_box_page):
    #TC-CheckBox-005
    #Launch the Check Box page
    check_box_page.navigate()

    #Expand the root checkbox
    check_box_page.expand_root()

    #Expand the "Documents" checkbox
    check_box_page.expand_Documents()

    #Expand the "Workspace" checkbox
    check_box_page.expand_Workspace()

    #Expand the "Angular" checkbox
    check_box_page.uncheck_Angular()