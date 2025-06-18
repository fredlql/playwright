from utils.helpers import login, logout

def test_login_logout(browser_page):
    login(browser_page)
    assert browser_page.is_visible(".shopping_cart_link")
    logout(browser_page)
    assert browser_page.url == "https://www.saucedemo.com/"

