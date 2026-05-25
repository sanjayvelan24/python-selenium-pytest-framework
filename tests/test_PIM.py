import pytest
from pages.PIMPage import PIMpage
from pages.LoginPage import Loginpage
from config.config import BASE_URL

class TestPIM:
    @pytest.mark.skip(reason="demo site unreliable on CI")
    def test_PIM(self, setup):
        self.driver = setup

        self.driver.get(BASE_URL)
        #login
        self.lp = Loginpage(self.driver)
        self.lp.setusername("Admin")
        self.lp.setpassword("admin123")
        self.lp.clicklogin()

        self.P = PIMpage(self.driver)
        self.P.clickPIMbutton()
        self.P.clickAddEmployeebutton()

        self.P.add_employee_details("sanjay","v", "velan", "02424")
        self.P.clicksave_button()
        try:
            self.toaster_message = self.P.verify_toaster()
            assert "Successfully Saved" in self.toaster_message , f"Toaster message is wrong {self.toaster_message}"
            print(f"Tosater message is : {self.toaster_message}")
        except Exception as e :
            print(f"Toaster not caught - it may have disappeared: {e}")
        self.P.wait_for_toaster_disappear() 
        
        self.actual_firstname = self.P.get_firstname()
        self.actual_middlename = self.P.get_middlename()
        self.actual_lastname = self.P.get_lastname()
        self.actual_employeeid = self.P.get_employeeid()

        assert self.actual_firstname == "sanjay", f"Actual result is : {self.actual_firstname}"
        assert self.actual_middlename == "v", f"Actual result is : {self.actual_middlename}"
        assert self.actual_lastname =="velan", f"Actual result is : {self.actual_lastname}"
        assert self.actual_employeeid == "02424", f"Actual result is : {self.actual_employeeid}"

        self.P.click_employee_list()
        # self.result = self.P.is_record_present("sanjay")
        # assert self.result == "Sanjay", "Sanjay not found in eomployee table"
        assert self.P.is_record_present("sanjay v"), "Sanjay not found in employee table"
        