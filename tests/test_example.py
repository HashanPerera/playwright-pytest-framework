""" from pages.google_page import GooglePage

def test_google_title(page):
    google_page = GooglePage(page)
    google_page.navigate()
    assert "Google" in page.title()


def test_google_search_box(page):

    #Launch the Google homepage
    google_page = GooglePage(page)
    google_page.navigate()
    
    #Click the "Reject all" button to dismiss the cookie consent banner
    google_page.dismiss_cookie_banner()

    #Get the search box and perform a search for "Playwright"
    search_box = google_page.search("Halo:Reach")
   """