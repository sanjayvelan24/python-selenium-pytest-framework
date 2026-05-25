import pytest
from pages.LoginPage import Loginpage
from pages.LogoutPage import LogOut
from selenium.webdriver.common.by import By
from config.config import BASE_URL


class TestLogout:
    @pytest.mark.skip(reason="demo site unreliable on CI")
    def test_logout(self, setup):

        self.driver = setup

        self.driver.get(BASE_URL)        
        self.lp = Loginpage(self.driver)
        self.lp.setusername("Admin")
        self.lp.setpassword("admin123")
        self.lp.clicklogin()
        assert self.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").is_displayed()

        self.lo= LogOut(self.driver)
        self.lo.clickprofile()
        self.lo.clicklogout()

        assert "login" in self.driver.current_url.lower()
