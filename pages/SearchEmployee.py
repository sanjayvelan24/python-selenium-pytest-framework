from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Search_Employee:
    #locators
    button_menuPIM_Xpath = (By.XPATH,"//span[normalize-space() = 'PIM']")
    txtemployeeid_Xpath = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    button_search_Xpath = (By.XPATH,"//button[normalize-space()='Search']")
    toaster_Xpath = (By.XPATH,"//div[@id='oxd-toaster_1']")
    record_count_Xpath = (By.XPATH, "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/span")
    table_row_Xpath = (By.XPATH, "//div[@class='oxd-table-card']")
    # table_cell_Xpath = (By.XPATH, "//div[@role='cell'][2]]")
    button_reset_Xpath = (By.XPATH, "//button[normalize-space()='Reset']")

    #Constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    #Actions
    def clickPIMbutton(self):
        self.wait.until(EC.element_to_be_clickable(self.button_menuPIM_Xpath)).click()
    
    def set_employee_id(self, employeeid):
       self.employee_id = self.wait.until(EC.visibility_of_element_located(self.txtemployeeid_Xpath))
       self.employee_id.click()
       self.employee_id.send_keys(Keys.CONTROL+'a')
       self.employee_id.send_keys(Keys.DELETE)
       self.employee_id.send_keys(employeeid)
    
    def click_search_button(self):
        self.wait.until(EC.element_to_be_clickable(self.button_search_Xpath)).click()
    
    def verify_toaster(self):
        toaster = self.wait.until(EC.visibility_of_element_located(self.toaster_Xpath))
        return toaster.text

    def verify_record_count(self):
        record_count = self.wait.until(EC.visibility_of_element_located(self.record_count_Xpath))
        return record_count.text
    
    def verify_result(self,employeeid):
        rows = self.wait.until(EC.visibility_of_all_elements_located(self.table_row_Xpath))

        if len(rows) == 0:
            print("No Record found")
            return False
        for row in rows:
            if employeeid in row.text:
                print(f"record found : {employeeid}")
                return True
        print(f"Record not found {employeeid}")
        return True
    
    def click_reset_button(self):
        self.wait.until(EC.element_to_be_clickable(self.button_reset_Xpath)).click()

    def verify_reset_button(self):
        field_value = self.wait.until(EC.visibility_of_element_located(self.txtemployeeid_Xpath)).get_attribute("value")

        if field_value == "":
            print("Reset is succesfull")
            return True
        else:
            print(f"Reset  failed : {field_value}")
            return False    
