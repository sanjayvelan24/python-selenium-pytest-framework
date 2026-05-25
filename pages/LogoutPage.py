from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogOut :
    #locators
    profile_button_Xpath = (By.XPATH,"//p[@class='oxd-userdropdown-name']")
    logout_button_Xpath = (By.XPATH,"//a[normalize-space() = 'Logout']")
    # txtbox_username = (By.XPATH, "//input[@name='username']")
    # txtbox_password = (By.XPATH, "//input[@name='password']")
    # button_login =(By.XPATH,"//input[@name='password']/ancestor::form/descendant::button")

    #constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
    
    #actions
    # def setusername(self,username):
    #     usernametxt = self.wait.until(EC.visibility_of_element_located(self.txtbox_username))
    #     usernametxt.send_keys(username)
    
    # def setpassword(self, pwd):
    #     passwordtxt = self.wait.until(EC.visibility_of_element_located(self.txtbox_password))
    #     passwordtxt.send_keys(pwd)

    # def clicklogin(self):
    #     loginButton = self.wait.until(EC.element_to_be_clickable(self.button_login))
    #     loginButton.click()

    def clickprofile(self):
        clickprofilebutton = self.wait.until(EC.element_to_be_clickable(self.profile_button_Xpath))
        clickprofilebutton.click()

    def clicklogout(self):
        clicklogoutbutton = self.wait.until(EC.element_to_be_clickable(self.logout_button_Xpath))    
        clicklogoutbutton.click()