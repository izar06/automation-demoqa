from playwright.sync_api import sync_playwright
import pytest
import allure


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.goto("https://katalon-demo-cura.herokuapp.com/")
        yield page
        screenshoot = page.screenshot(full_page=True)
        allure.attach(screenshoot, "Hasil Akhir", attachment_type=allure.attachment_type.PNG)
        browser.close()