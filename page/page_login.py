from locator.loc_page_login import LocatorLogin
import allure

class Login:
    def __init__(self, page):
        self.page = page
    
    def input_email(self, email):
        with allure.step("Input Email"):
            self.page.locator(LocatorLogin.input_email).fill(email)
        
    def input_password(self, password):
        with allure.step("Input Password"):
            self.page.locator(LocatorLogin.input_password).fill(password)
    
    def click_btn_login(self):
        with allure.step("Click Button Login"):
            self.page.locator(LocatorLogin.btn_login).click()
        
    def error_msg(self):
        error_msg = self.page.locator(LocatorLogin.error_msg).text_content()
        return error_msg
    
    def check_field_email(self):
        error_field_email = self.page.locator(LocatorLogin.input_email).evaluate("el => el.validationMessage")
        return error_field_email
    
    def check_field_password_empty(self):
        error_field_password_empty = self.page.locator(LocatorLogin.input_password).evaluate("el => el.validationMessage")
        return error_field_password_empty