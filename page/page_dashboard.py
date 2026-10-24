from locator.loc_page_dashboard import LocatorDashboard

class Dashboard:
    def __init__(self, page):
        self.page = page
    
    def select_facility(self, facility: str):
        self.page.select_option(LocatorDashboard.facility, label=facility)

    def check_readmission(self):
        self.page.check(LocatorDashboard.check_readmission)

    def select_program(self, program: str):
        # program: "medicare", "medicaid", atau "none"
        self.page.check(f"#radio_program_{program.lower()}")

    def input_visit_date(self, date: str):
        field = self.page.locator(LocatorDashboard.visit_date)
        field.click()
        field.press_sequentially(date, delay=100)
        self.page.keyboard.press("Enter")

    def input_comment(self, text: str):
        self.page.fill(LocatorDashboard.comment, text)

    def click_book(self):
        self.page.click(LocatorDashboard.btn_book)
    
    def assertion(self):
        title = self.page.locator(LocatorDashboard.title_dahsboard).text_content()
        return title