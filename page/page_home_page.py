from locator.loc_home_page import LocatorHomePage
import allure





class HomePage:
    def __init__(self, page):
        self.page = page
    
    
    def click_hamburger_menu(self):
        with allure.step("Hamburger Menu"):
            self.page.locator(LocatorHomePage.hamburger_menu).click()
            
    def click_login(self):
        with allure.step("Hamburger Menu"):
            self.page.locator(LocatorHomePage.btn_login).click()
    