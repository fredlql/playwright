from utils.helpers import login

def test_checkout(browser_page):
    login(browser_page)

    # Ajouter produit
    browser_page.click("button[data-test='add-to-cart-sauce-labs-bike-light']")
    browser_page.click(".shopping_cart_link")
    assert browser_page.is_visible("text=Sauce Labs Bike Light")

    # Checkout
    browser_page.click("button[data-test='checkout']")
    browser_page.fill("input[data-test='firstName']", "John")
    browser_page.fill("input[data-test='lastName']", "Doe")
    browser_page.fill("input[data-test='postalCode']", "75000")
    browser_page.click("input[data-test='continue']")

    # Vérif total
    total_text = browser_page.text_content(".summary_total_label")
    assert "Total" in total_text

    # Finish
    browser_page.click("button[data-test='finish']")
    assert browser_page.is_visible("text=THANK YOU FOR YOUR ORDER")
    browser_page.screenshot(path="screenshots/confirmation.png")

