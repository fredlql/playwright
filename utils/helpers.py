from playwright.sync_api import Page

def login(page: Page, username="standard_user", password="secret_sauce"):
    page.goto("https://www.saucedemo.com/")
    page.fill("input[data-test='username']", username)
    page.fill("input[data-test='password']", password)
    page.click("input[data-test='login-button']")
    assert "inventory" in page.url, "Échec de la connexion"

def logout(page: Page):
    page.click("#react-burger-menu-btn")
    page.wait_for_selector("#logout_sidebar_link")
    page.click("#logout_sidebar_link")

