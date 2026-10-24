from playwright.sync_api import expect
from page.page_login import Login
from page.page_dashboard import Dashboard
from page.page_home_page import HomePage
from locator.loc_page_login import LocatorLogin
from locator.loc_page_dashboard import LocatorDashboard
from helper.helper import attach_screenshot
import allure

@allure.feature("Login")
@allure.story("Login tidak valid")
def test_login_invalid(page):
    home = HomePage(page)
    login = Login(page)
    dashboard = Dashboard(page)

    with allure.step("Klik menu hamburger"):
        home.click_hamburger_menu()
        attach_screenshot(page, "Menu hamburger")

    with allure.step("Klik Login"):
        home.click_login()
        attach_screenshot(page, "Halaman login")

    with allure.step("Input username"):
        login.input_email("John Chonor")
        attach_screenshot(page, "Input username")

    with allure.step("Input password"):
        login.input_password("password")
        attach_screenshot(page, "Input password")

    with allure.step("Klik tombol Login"):
        login.click_btn_login()
        attach_screenshot(page, "Setelah klik Login")

    with allure.step("Cek pesan error"):
        # Expectation Playwright
        expect(page.locator(LocatorLogin.error_msg)).to_be_visible()

        error = login.error_msg()
        print(error)
        assert error == "Login failed! Please ensure the username and password are valid."
        attach_screenshot(page, "Pesan error")


@allure.feature("Login")
@allure.story("Login valid")
def test_login(page):
    home = HomePage(page)
    login = Login(page)
    dashboard = Dashboard(page)

    with allure.step("Klik menu hamburger"):
        home.click_hamburger_menu()
        attach_screenshot(page, "Menu hamburger")

    with allure.step("Klik Login"):
        home.click_login()
        attach_screenshot(page, "Halaman login")

    with allure.step("Input username"):
        login.input_email("John Doe")
        attach_screenshot(page, "Input username")

    with allure.step("Input password"):
        login.input_password("ThisIsNotAPassword")
        attach_screenshot(page, "Input password")

    with allure.step("Klik tombol Login"):
        login.click_btn_login()
        attach_screenshot(page, "Setelah klik Login")

    with allure.step("Cek halaman Make Appointment"):
        # Expectation Playwright
        expect(page.locator("h2")).to_have_text("Make Appointment")

        # Expectation Pytest
        title = dashboard.assertion()
        print(title)
        assert title == "Make Appointment"
        attach_screenshot(page, "Make Appointment")


@allure.feature("Appointment")
@allure.story("Make appointment berhasil")
def test_make_appointment_valid(page):
    home = HomePage(page)
    login = Login(page)
    dashboard = Dashboard(page)

    with allure.step("Klik menu hamburger"):
        home.click_hamburger_menu()
        attach_screenshot(page, "Menu hamburger")

    with allure.step("Klik Login"):
        home.click_login()
        attach_screenshot(page, "Halaman login")

    with allure.step("Input username"):
        login.input_email("John Doe")
        attach_screenshot(page, "Input username")

    with allure.step("Input password"):
        login.input_password("ThisIsNotAPassword")
        attach_screenshot(page, "Input password")

    with allure.step("Klik tombol Login"):
        login.click_btn_login()
        attach_screenshot(page, "Setelah klik Login")

    with allure.step("Pilih facility"):
        dashboard.select_facility("Seoul CURA Healthcare Center")
        attach_screenshot(page, "Pilih facility")

    with allure.step("Centang readmission"):
        dashboard.check_readmission()
        attach_screenshot(page, "Readmission")

    with allure.step("Pilih program"):
        dashboard.select_program("medicare")
        attach_screenshot(page, "Pilih program")

    with allure.step("Input visit date"):
        dashboard.input_visit_date("30/10/2026")
        attach_screenshot(page, "Input visit date")

    with allure.step("Input comment"):
        dashboard.input_comment("test")
        attach_screenshot(page, "Input comment")

    with allure.step("Klik Book Appointment"):
        dashboard.click_book()
        attach_screenshot(page, "Setelah klik Book")

    with allure.step("Cek halaman Appointment Confirmation"):
        # Expectation Playwright
        expect(page.locator("h2")).to_have_text("Appointment Confirmation")
        attach_screenshot(page, "Appointment Confirmation")


@allure.feature("Appointment")
@allure.story("Visit date kosong")
def test_make_appointment_tanpa_visit_date(page):
    home = HomePage(page)
    login = Login(page)
    dashboard = Dashboard(page)

    with allure.step("Klik menu hamburger"):
        home.click_hamburger_menu()
        attach_screenshot(page, "Menu hamburger")

    with allure.step("Klik Login"):
        home.click_login()
        attach_screenshot(page, "Halaman login")

    with allure.step("Input username"):
        login.input_email("John Doe")
        attach_screenshot(page, "Input username")

    with allure.step("Input password"):
        login.input_password("ThisIsNotAPassword")
        attach_screenshot(page, "Input password")

    with allure.step("Klik tombol Login"):
        login.click_btn_login()
        attach_screenshot(page, "Setelah klik Login")

    with allure.step("Pilih facility"):
        dashboard.select_facility("Tokyo CURA Healthcare Center")
        attach_screenshot(page, "Pilih facility")

    with allure.step("Pilih program"):
        dashboard.select_program("medicare")
        attach_screenshot(page, "Pilih program")

    with allure.step("Input comment"):
        dashboard.input_comment("tanpa tanggal")
        attach_screenshot(page, "Input comment")

    with allure.step("Klik Book Appointment"):
        dashboard.click_book()
        attach_screenshot(page, "Setelah klik Book")

    with allure.step("Cek tetap di halaman dashboard"):
        # Field required: halaman tidak pindah ke summary
        expect(page.locator(LocatorDashboard.title_dahsboard)).to_be_visible()
        attach_screenshot(page, "Field required")
