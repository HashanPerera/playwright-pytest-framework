
def test_Add_data(web_table_page):
    web_table_page.navigate()
    web_table_page.fill_form(web_table_page.form_data)

def test_Search_data(web_table_page):
    web_table_page.navigate()
    web_table_page.search_record()
 
def test_Edit_record(web_table_page):
    web_table_page.navigate()
    web_table_page.edit_record()

def test_delete_record(web_table_page):
    web_table_page.navigate()
    web_table_page.delete_table_row()