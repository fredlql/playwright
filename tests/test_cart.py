from utils.helpers import login

def test_add_to_cart(browser_page):
    login(browser_page)
    browser_page.click("button[data-test='add-to-cart-sauce-labs-backpack']")
    browser_page.click(".shopping_cart_link")
    assert browser_page.is_visible("text=Sauce Labs Backpack")
    browser_page.screenshot(path="screenshots/panier.png")

