import pytest
from pages.SearchEmployee import Search_Employee
from pages.LoginPage import Loginpage
from config.config import BASE_URL

class TestSearchEmployee:
    @pytest.mark.skip(reason="demo site unreliable on CI")
    def test_searchemployee(self, setup):
        self.driver = setup
        self.driver.get(BASE_URL)
        #login
        self.lp = Loginpage(self.driver)
        self.lp.setusername("Admin")
        self.lp.setpassword("admin123")
        self.lp.clicklogin()

        self.Se = Search_Employee(self.driver)
        self.Se.clickPIMbutton()
        self.Se.set_employee_id("0295")
        self.Se.click_search_button()
        try:
            self.toaster_msg = self.Se.verify_toaster()
            print(f"toster :{self.toaster_msg}")
        except:
            self.count = self.Se.verify_record_count()
            print(f"Recount count is : {self.count}")
        self.verifydata =self.Se.verify_result("0295")
        assert self.verifydata,"searched data is not found"

        
        self.Se.click_reset_button()
        result = self.Se.verify_reset_button()
        assert result ,"Reset did not cleared "
            




