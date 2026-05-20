import pytest
from pages.LoginPage import Loginpage
from config.config import BASE_URL

class Testlogin:
    def test_login(self, setup):
        self.driver = setup

        self.driver.get(BASE_URL)        
        self.lp = Loginpage(self.driver)
        self.lp.setusername("Admin")
        self.lp.setpassword("admin123")
        self.lp.clicklogin()

        self.actual_title= self.driver.title

        assert self.actual_title == "OrangeHRM", f"Expected 'OrangeHRM' but got : {self.actual_title}"
